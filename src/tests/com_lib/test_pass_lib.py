# -*- coding: utf-8 -*-
import unittest

from com_lib.pass_lib import encrypt_pass, verify_pass


class Test(unittest.TestCase):
    def test_encrypt_password(self):
        password = "toast"
        hashed_pwd = encrypt_pass(password)

        assert type(hashed_pwd) is str

    def test_verify_password(self):
        pwd = "toast"
        crypt_pwd = encrypt_pass(pwd)

        result = verify_pass(pwd, crypt_pwd)
        assert result == True

    def test_verify_password_incorrect(self):
        pwd = "toast"
        crypt_pwd = encrypt_pass(pwd)

        pwd_fail = "toasT"
        result = verify_pass(pwd_fail, crypt_pwd)
        assert result == False
