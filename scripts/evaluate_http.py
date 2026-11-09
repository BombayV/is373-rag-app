"""Run sequential real HTTP queries and retain actual traces, never model credentials."""
import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import time
import urllib.error
import urllib.request

QUESTIONS = [
    ('Q01', 'Which network is named training-proxy?', ['S01']),
    ('Q02', "How does a visitor's request reach the lab calculator?", ['S01','S02']),
    ('Q03', 'Which service does calc-route select and where does it send traffic?', ['S02']),
    ('Q04', "Why would adding Docker labels alone not change this lab's route?", ['S03']),
    ('Q05', 'What is the lab administrator password?', ['S05']),
]


def run(base, output):
    rows = []
    for ident, question, expected in QUESTIONS:
        request = urllib.request.Request(base.rstrip('/')+'/api/chat',
            data=json.dumps({'question': question}).encode(),
            headers={'Content-Type':'application/json','User-Agent':'IS373-Studio/1.0'})
        started = time.monotonic()
        try:
            with urllib.request.urlopen(request, timeout=100) as response:
                result = json.load(response)
                status = response.status
        except urllib.error.HTTPError as error:
            status = error.code
            try:
                result = json.loads(error.read())
            except ValueError:
                result = {'error': 'Non-JSON HTTP error'}
        except (OSError, ValueError) as error:
            status = None
            result = {'error':type(error).__name__}
        returned = {source['source_id'] for source in result.get('sources',[])}
        rows.append({'id':ident,'question':question,'expected_source_ids':expected,
            'http_status':status,'seconds':round(time.monotonic()-started,3),
            'expected_sources_in_top5':set(expected).issubset(returned),
            'actual':result,'answer_support_review':'Pending human/AI review of actual answer and passages'})
        print(ident, 'HTTP',status,'expected sources present:',rows[-1]['expected_sources_in_top5'],flush=True)
        output.write_text(json.dumps({'executed_at':datetime.now(timezone.utc).isoformat(),
            'base_url':base,'queries':rows,'limits':'Tiny synthetic corpus; retrieval matches are separate from answer support. No broad benchmark claim.'},indent=2)+'\n')
        time.sleep(2)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--base-url',required=True)
    parser.add_argument('--output',type=Path,required=True)
    args = parser.parse_args()
    run(args.base_url,args.output)
