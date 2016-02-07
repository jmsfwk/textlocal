import os
import unittest

from textlocal import Textlocal


API_KEY = os.environ['API_KEY']


class TextlocalTest(unittest.TestCase):

    def setUp(self):
        self.textlocal = Textlocal(api_key=API_KEY)

    def test_init_api_key(self):
        with self.assertRaises(Exception):
            textlocal = Textlocal()
        textlocal = Textlocal(api_key=API_KEY)
        self.assertEqual(type(textlocal), Textlocal)

    def test_init_password_username(self):
        with self.assertRaises(Exception):
            textlocal = Textlocal(username='username')
        with self.assertRaises(Exception):
            textlocal = Textlocal(password='password')
        textlocal = Textlocal(username='username', password='password')
        self.assertEqual(type(textlocal), Textlocal)

    def test_get_credentials_returns_dict(self):
        USERNAME = 'username'
        PASSWORD = 'password'
        textlocal = Textlocal(api_key=API_KEY)
        credentials = textlocal._get_credentials()
        self.assertIsInstance(credentials, dict)
        textlocal = Textlocal(username=USERNAME, password=PASSWORD)
        credentials = textlocal._get_credentials()
        self.assertIsInstance(credentials, dict)

    def test_get_credentials_returns_credentials(self):
        USERNAME = 'username'
        PASSWORD = 'password'
        textlocal = Textlocal(api_key=API_KEY)
        credentials = textlocal._get_credentials()
        self.assertEqual(credentials['apiKey'], API_KEY)
        textlocal = Textlocal(username=USERNAME, password=PASSWORD)
        credentials = textlocal._get_credentials()
        self.assertEqual(credentials['username'], USERNAME)
        self.assertEqual(credentials['hash'], PASSWORD)
        textlocal = Textlocal(api_key=API_KEY,
                              username=USERNAME,
                              password=PASSWORD)
        credentials = textlocal._get_credentials()
        self.assertEqual(credentials['apiKey'], API_KEY)

    def test_get_credentials_prefers_api_key(self):
        USERNAME = 'username'
        PASSWORD = 'password'
        textlocal = Textlocal(api_key=API_KEY,
                              username=USERNAME,
                              password=PASSWORD)
        credentials = textlocal._get_credentials()
        self.assertEqual(len(credentials), 1)

    def test_call(self):
        response = self.textlocal._call('get', '')
        self.assertIsInstance(response, dict)
        self.assertEqual(len(response), 2)
        self.assertEqual(response['status'], 'failure')

    def test_get_balance_returns_tuple(self):
        balance = self.textlocal.get_balance()
        self.assertIsInstance(balance, tuple)

    def test_get_balance_tuple_has_length_two(self):
        balance = self.textlocal.get_balance()
        self.assertEqual(len(balance), 2)

    def test_get_balance_returns_ints(self):
        balance = self.textlocal.get_balance()
        self.assertIsInstance(balance[0], int)
        self.assertIsInstance(balance[1], int)

    def test_get_templates_returns_list(self):
        templates = self.textlocal.get_templates()
        self.assertIsInstance(templates, list)

if __name__ == '__main__':
    unittest.main()
