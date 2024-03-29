import json
from datetime import datetime

from Note import Note



class NoteSerializer:
    @staticmethod
    def serialize(note):
        return json.dumps(note.to_dict())

    @staticmethod
    def deserialize(data):
        note_data = json.loads(data)
        timestamp = datetime.strptime(note_data['timestamp'], "%d-%m-%Y %H:%M:%S")
        return Note(note_data['title'], note_data['body'], timestamp)
