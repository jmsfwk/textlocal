import unittest

from textlocal import Textlocal


class TextlocalTest(unittest.TestCase):

    def setUp(self):
        self.textlocal = Textlocal(api_key='vpvejpIVqYc'
                                   '-EJuZMiGpno9Mnz9qDhMT05qF8ol7pu')

    def test_init_api_key(self):
        with self.assertRaises(Exception):
            textlocal = Textlocal()
        textlocal = Textlocal(
            api_key='vpvejpIVqYc-EJuZMiGpno9Mnz9qDhMT05qF8ol7pu')
        self.assertEqual(type(textlocal), Textlocal)

    def test_init_password_username(self):
        with self.assertRaises(Exception):
            textlocal = Textlocal(username='username')
        with self.assertRaises(Exception):
            textlocal = Textlocal(password='password')
        textlocal = Textlocal(username='username', password='password')
        self.assertEqual(type(textlocal), Textlocal)

    def test_get_credentials_returns_dict(self):
        API_KEY = 'api_key'
        USERNAME = 'username'
        PASSWORD = 'password'
        textlocal = Textlocal(api_key=API_KEY)
        credentials = textlocal._get_credentials()
        self.assertIsInstance(credentials, dict)
        textlocal = Textlocal(username=USERNAME, password=PASSWORD)
        credentials = textlocal._get_credentials()
        self.assertIsInstance(credentials, dict)

    def test_get_credentials_returns_credentials(self):
        API_KEY = 'api_key'
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
        API_KEY = 'api_key'
        USERNAME = 'username'
        PASSWORD = 'password'
        textlocal = Textlocal(api_key=API_KEY,
                              username=USERNAME,
                              password=PASSWORD)
        credentials = textlocal._get_credentials()
        self.assertEqual(len(credentials), 1)

    def test_call(self):
        pass

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

if __name__ == '__main__':
    unittest.main()
