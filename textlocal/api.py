import json
import urllib.parse

import requests

import json

class Textlocal(object):
    DOMAIN = 'https://api.txtlocal.com'

    def __init__(self, api_key=None, username=None, password=None):
        if api_key == username == password == None:
            raise Exception("Either api_key or username and password must be used.")
        elif (username is None and password is not None) or (password is None and username is not None):
            raise Exception("If using username and password both must be set.")
        self.api_key = api_key
        self.username = username
        self.password = password

    def get_balance(self):
        """
        Gets the credit balance

        Returns as two-tuple in the form `(sms, mms)`.
        """
        PATHNAME = 'balance'
        response = self._call(PATHNAME)
        balance = response.get('balance')
        return balance['sms'], balance['mms']

    def _call(self, pathname, data=None):
        """
        Makes a request to the textlocal api. Returns a JSON string.
        """
        url = urllib.parse.urljoin(self.DOMAIN, pathname)
        if data:
            data.update(self._get_credentials())
        else:
            data = self._get_credentials()
        data['test'] = 'true'
        r = requests.post(url, data)
        return r.json()

    def _get_credentials(self):
        """
        Creates a dictionary of the api credentials

        Prefers an api key over username/password.
        """
        if self.api_key:
            return {'apiKey' : self.api_key}
        else:
            return {'username': self.username, 'hash' : self.password}
