import json
from datetime import datetime

from Note import Note
from NoteSerializer import NoteSerializer


class NoteManager:
    def __init__(self, filename):
        self.filename = filename

    def load_notes(self):
        try:
            with open(self.filename, 'r') as file:
                notes_data = json.load(file)
                return [NoteSerializer.deserialize(note_data) for note_data in notes_data]
        except FileNotFoundError:
            return []

    def save_notes(self, notes):
        with open(self.filename, 'w') as file:
            serialized_notes = [NoteSerializer.serialize(note) for note in notes]
            json.dump(serialized_notes, file)

    def add_note(self, note):
        notes = self.load_notes()
        notes.append(note)
        self.save_notes(notes)

    def list_notes(self):
        notes = self.load_notes()
        for idx, note in enumerate(notes, start=1):
            print(f"ID: {idx}, Title: {note.title}, Timestamp: {note.timestamp.strftime('%d-%m-%Y %H:%M:%S')}")

    def edit_note(self, note_id, new_note):
        notes = self.load_notes()
        if 1 <= note_id <= len(notes):
            notes[note_id - 1] = new_note
            self.save_notes(notes)
            return True
        return False

    def delete_note(self, note_id):
        notes = self.load_notes()
        if 1 <= note_id <= len(notes):
            del notes[note_id - 1]
            self.save_notes(notes)
            return True
        return False

    def get_note_body(self, note_id):
        notes = self.load_notes()
        if 1 <= note_id <= len(notes):
            return notes[note_id - 1].body
        return None

    def filter_notes_by_date(self, date):
        notes = self.load_notes()
        filtered_notes = [note for note in notes if note.timestamp.date() == date.date()]
        return filtered_notes


if __name__ == "__main__":
    manager = NoteManager("notes.json")

    while True:
        command = input('\033[43m<Здравствуйте и добро пожаловать в консольное приложение Земетки!>\033[0m\n\n'
                        '\033[32m<Введите интересующую Вас команду>\033[0m\n\n'
                        '****************************************************************\n'
                        'add  - создание заметки\n'
                        'list - просмотр заметки\n'
                        'list_by_date - просмотр заметки по дате\n'
                        'edit - редактирование заметки \n'
                        'delete - удаление заметки\n'
                        'read - чтение заметки\n'
                        'exit - выход\n\n').strip().lower()

        if command == 'add':
            title = input("Введите заголовок заметки: ").strip()
            body = input("Введите тело заметки: ").strip()
            note = Note(title, body)
            manager.add_note(note)
            print("Заметка успешно добавлена.")

        elif command == 'list':
            manager.list_notes()

        elif command == 'list_by_date':
            date_str = input("Введите дату в формате ДД-ММ-ГГГГ: ")
            date = datetime.strptime(date_str, "%d-%m-%Y")
            filtered_notes = manager.filter_notes_by_date(date)
            for idx, note in enumerate(filtered_notes, start=1):
                print(f"ID: {idx}, Title: {note.title}, Timestamp: {note.timestamp}")

        elif command == 'edit':
            note_id = int(input("Введите ID заметки для редактирования: "))
            title = input("Введите новый заголовок заметки: ").strip()
            body = input("Введите новое тело заметки: ").strip()
            new_note = Note(title, body)
            if manager.edit_note(note_id, new_note):
                print("Заметка успешно отредактирована.")
            else:
                print("Заметка с указанным ID не найдена.")

        elif command == 'delete':
            note_id = int(input("Введите ID заметки для удаления: "))
            if manager.delete_note(note_id):
                print("Заметка успешно удалена.")
            else:
                print("Заметка с указанным ID не найдена.")

        elif command == 'read':
            note_id = int(input("Введите ID заметки для прочтения: "))
            note_body = manager.get_note_body(note_id)
            if note_body:
                print("Тело заметки:")
                print(note_body)
            else:
                print("Заметка с указанным ID не найдена.")

        elif command == 'exit':
            print("Программа завершена.")
            break

        else:
            print("Некорректная команда. Пожалуйста, попробуйте снова.")