from datetime import datetime


class Note:
    def __init__(self, title, body, timestamp=None):
        self.title = title
        self.body = body
        self.timestamp = timestamp if timestamp else datetime.now()

    def to_dict(self):
        return {
            'title': self.title,
            'body': self.body,
            'timestamp': self.timestamp.strftime("%d-%m-%Y %H:%M:%S")
        }
