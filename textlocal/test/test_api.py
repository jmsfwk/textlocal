import unittest

from textlocal import Textlocal


class TextlocalTest(unittest.TestCase):

    def test_init_hash(self):
        with self.assertRaises(Exception):
            textlocal = Textlocal()
        textlocal = Textlocal(hash_code='hash')
        self.assertEqual(type(textlocal), Textlocal)

    def test_init_password_username(self):
        with self.assertRaises(Exception):
            textlocal = Textlocal(username='username')
        with self.assertRaises(Exception):
            textlocal = Textlocal(password='password')
        textlocal = Textlocal(username='username', password='password')
        self.assertEqual(type(textlocal), Textlocal)

    def test_get_balance(self):
        textlocal = Textlocal(hash_code='hash')
        print(textlocal.get_balance())

if __name__ == '__main__':
    unittest.main()
