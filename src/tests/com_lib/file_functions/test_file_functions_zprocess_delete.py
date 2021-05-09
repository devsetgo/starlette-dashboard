# -*- coding: utf-8 -*-
# import json
# import csv
import datetime
import unittest

import pytest

from com_lib.file_functions import (
    create_sample_files,
    delete_file,
    get_data_directory_list,
    open_csv,
    open_json,
    open_text,
    save_csv,
    save_json,
    save_text,
)

time_str = datetime.datetime.now()


class Test(unittest.TestCase):
    def test_delete_csv_test_one(self):
        file_named = "test_1.csv"
        result = delete_file(file_named)
        assert result == "complete"

    def test_delete_csv_test_sample(self):
        file_named = "test_sample.csv"
        result = delete_file(file_named)
        assert result == "complete"

    def test_delete_json_test_one(self):
        file_named = "test_1.json"
        result = delete_file(file_named)
        assert result == "complete"

    def test_delete_json_test_sample(self):
        file_named = "test_sample.json"
        result = delete_file(file_named)
        assert result == "complete"

    def test_delete_text_test_one(self):
        file_named = "test_1.html"
        result = delete_file(file_named)
        assert result == "complete"

    def test_delete_type_error(self):
        file_named = ["test_sample.csv"]
        with pytest.raises(Exception):
            assert delete_file(file_named)

    def test_delete_csv_notfound_error(self):
        file_named = "error_file.csv"
        with pytest.raises(Exception):
            assert delete_file(file_named)

    def test_delete_json_notfound_error(self):
        file_named = "error_file.json"
        with pytest.raises(Exception):
            assert delete_file(file_named)

    def test_delete_text_notfound_error(self):
        file_named = "error_file.txt"
        with pytest.raises(Exception):
            assert delete_file(file_named)

    def test_delete_no_slash_error(self):
        file_named = r"\error_file.csv"
        with pytest.raises(Exception):
            assert delete_file(file_named)

    def test_delete_no_slash_two_error(self):
        file_named = r"/error_file.csv"
        with pytest.raises(Exception):
            assert delete_file(file_named)
