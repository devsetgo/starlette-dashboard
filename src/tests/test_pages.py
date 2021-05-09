# -*- coding: utf-8 -*-
import unittest
import uuid

from starlette.testclient import TestClient

from main import app

client = TestClient(app)


class Test(unittest.TestCase):
    def test_pages(self):
        pages = ["calendar", "gallery", "widgets"]

        for page in pages:
            url = f"/pages/{page}"
            client = TestClient(app)
            response = client.get(url)
            assert response.status_code == 200

    def test_pages_error(self):
        uid = uuid.uuid4()
        url = f"/pages/{uid}"
        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 404
