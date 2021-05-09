# -*- coding: utf-8 -*-
import unittest

from starlette.testclient import TestClient

from app.main import app
from routes.pages.functions import call_api

client = TestClient(app)


class Test(unittest.TestCase):
    def test_call_api(self):
        # with pytest.raises(Exception):
        result = call_api()
        assert len(result) != 0

    # def test_call_api_error(self):

    #     with pytest.raises(Exception):
    #         assert call_api()
