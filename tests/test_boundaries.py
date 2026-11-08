"""HTTP boundary tests; no provider or vector-store calls simulated as evidence."""
import os
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from fastapi.testclient import TestClient
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import app as guide


class Boundaries(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.data = patch.object(guide, 'DATA', Path(self.temp.name))
        self.data.start()
        self.client = TestClient(guide.app)

    def tearDown(self):
        self.data.stop()
        self.temp.cleanup()

    def test_public_page_and_status(self):
        self.assertEqual(self.client.get('/').status_code, 200)
        self.assertFalse(self.client.get('/health').json()['imported'])

    def test_missing_sources_does_not_invent_answer(self):
        response = self.client.post('/api/chat', json={'question':'Trace the lab route'})
        self.assertEqual(response.status_code, 503)
        self.assertNotIn('answer', response.json())

    def test_untrusted_input_is_bounded(self):
        self.assertEqual(self.client.post('/api/chat', json={'question':'x'*2001}).status_code,422)
        self.assertEqual(self.client.post('/api/chat',content=b'x'*9000).status_code,413)

    def test_import_is_not_public(self):
        self.assertEqual(self.client.post('/api/import').status_code,404)

    def test_missing_key_is_unavailable(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(guide.HTTPException) as error:
                guide.embed('a permitted fixture')
            self.assertEqual(error.exception.status_code,503)


if __name__ == '__main__':
    unittest.main()
