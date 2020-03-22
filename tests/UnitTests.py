import unittest
import sys
import os
sys.path.append(os.path.join(sys.path[0], '../RSA'))
from RSA import RSAalg
from random import randint

class RSATestCase(unittest.TestCase):
    def setUp(self):
        self.app = RSAalg()
        self.apps = [RSAalg() for i in range(1000)]

    def test_correct_encrypt_and_decrypt_int(self):
        n = randint(1, 1e6)
        self.assertEqual(n, self.app.decrypt_int(self.app.encrypt_int(n)))

    def test_correct_encrypt_and_decrypt_int_auto(self):
        for i in range(1000):
            n = randint(1, 1e9)
            self.assertEqual(n, self.app.decrypt_int(self.app.encrypt_int(n)))

    def test_correct_enc_and_dec_int_by_diff_auto(self):
        for i in range(10):
            n = randint(1, 1e6)
            for app in self.apps:
                self.assertEqual(n, app.decrypt_int(app.encrypt_int(n)))

    def test_correct_string(self):
        text = "Hello world!"
        self.assertEqual(text, self.app.decrypt_string(self.app.encrypt_string(text)))


if __name__ == '__main__':
    unittest.main()