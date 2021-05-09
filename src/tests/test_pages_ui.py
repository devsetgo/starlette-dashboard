# -*- coding: utf-8 -*-
import unittest
import uuid

from starlette.testclient import TestClient

from main import app

client = TestClient(app)


class Test(unittest.TestCase):
    def test_pages_ui(self):
        pages = [
            "buttons",
            "general",
            "icons",
            "modals",
            "navbar",
            "ribbons",
            "sliders",
            "timeline",
        ]

        for page in pages:
            url = f"/pages/ui/{page}"
            client = TestClient(app)
            response = client.get(url)
            assert response.status_code == 200

    def test_pages_ui_error(self):
        uid = uuid.uuid1()
        url = f"/pages/ui/{uid}"
        client = TestClient(app)
        response = client.get(url)
        assert response.status_code == 404
