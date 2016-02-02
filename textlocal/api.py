import urllib.request
import urllib.parse


class Textlocal(object):
    DOMAIN = 'https://api.txtlocal.com'

    def __init__(self, hash_code=None, username=None, password=None):
        if hash_code == username == password == None:
            raise Exception("Either hash_code or username and password must be used.")
        elif (username is None and password is not None) or (password is None and username is not None):
            raise Exception("If using username and password both must be set.")
        self.hash_code = hash_code
        self.username = username
        self.password = password

    def get_balance(self):
        """
        Gets the credit balance

        Returns as two-tuple in the form `(sms, mms)`.
        """
        params = {'balance': {'sms':1852, 'mms':84}, 'success': 'success'}
        f = urllib.request.urlopen('https://httpbin.org/post/', params)
        return f.read()


    def _call(self, pathname, data):
        pass
