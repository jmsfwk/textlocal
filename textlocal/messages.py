import base64


class Message(object):

    def __init__(self, message, numbers=None, group_id=None,
                 schedule_time=None, optouts=None):
        self.message = message
        self.numbers = numbers
        self.group_id = group_id
        self.schedule_time = schedule_time
        self.optouts = optouts


class MMS(Message):

    def __init__(self, message, numbers=None, group_id=None,
                 schedule_time=None, optouts=None, url=None, image=None):
        super(__class__, self).__init__(message, numbers, group_id,
                                        schedule_time, optouts)
        self.url = url
        if image is not None:
            self.encoded_image = base64.b64encode(image.read())

    def message_size(self):
        s = self.message.encode('utf8')
        return len(s)
