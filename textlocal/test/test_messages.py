import base64
import unittest

from textlocal.messages import MMS

class MMSTest(unittest.TestCase):

    def test_init_url(self):
        message_text = 'message'
        number = '4470123456789'
        url = 'http://example.com'
        message = MMS(message_text, [number,], url=url)
        self.assertEqual(message.url, url)

    def test_init_encoded_image(self):
        message_text = 'message'
        number = '4470123456789'
        file_name = __file__
        with open(file_name, 'rb') as test_file:
            message = MMS(message_text, [number,], image=test_file)
            test_file.seek(0)
            encoded_file = base64.b64encode(test_file.read())
        self.assertEqual(message.encoded_image, encoded_file)

    def test_message_size(self):
        message_text = 'message'
        number = '4470123456789'
        message = MMS(message_text, [number,])
        self.assertEqual(message.message_size(), 7)
        message.message = '𠜎'
        self.assertEqual(message.message_size(), 4)

if __name__ == '__main__':
    unittest.main()
