# -*- coding: utf-8 -*-
import unittest
import uuid

from starlette.testclient import TestClient

from main import app

client = TestClient(app)


class Test(unittest.TestCase):
    def test_health_pages(self):
        pages = ["status"]

        for page in pages:
            url = f"/health/{page}"
            client = TestClient(app)
            response = client.get(url)
            assert response.status_code == 200

    # def test_index__error(self):
    #     uid = uuid.uuid1()
    #     url = f"/index/{uid}"
    #     client = TestClient(app)
    #     response = client.get(url)
    #     assert response.status_code == 404
