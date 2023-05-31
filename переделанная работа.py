import json
import datetime

# Класс, описывающий заметку
class Note:
    def __init__(self, title, text, date):
        self.title = title
        self.text = text
        self.date = date

# Функция для создания заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    date_input = input("Введите дату заметки в формате ГГГГ.ММ.ДД: ")
    date = datetime.datetime.strptime(date_input, "%Y.%m.%d").date()
    note = Note(title, text, date)
    return note

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f, default=lambda o: o.__dict__, indent=4)

# Функция для загрузки заметок из файла
def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes_json = json.load(f)
            notes = []
            for note_json in notes_json:
                date = datetime.datetime.strptime(note_json['date'], "%Y-%m-%d").date()
                note = Note(note_json['title'], note_json['text'], date)
                notes.append(note)
    except FileNotFoundError:
        notes = []
    return notes

# Функция для чтения списка заметок
def read_notes(notes):
    for index, note in enumerate(notes):
        print(f"{index + 1}. {note.title} ({note.date.strftime('%Y.%m.%d')})")

# Функция для выборки заметок по дате
def filter_notes_by_date(notes):
    date_input = input("Введите дату для выборки в формате ГГГГ.ММ.ДД: ")
    date = datetime.datetime.strptime(date_input, "%Y.%m.%d").date()
    filtered_notes = [note for note in notes if note.date == date]
    return filtered_notes

# Функция для вывода заметки на экран
def display_note():
    index = int(input("Введите номер заметки для просмотра: "))
    note = notes[index - 1]
    print(f"{note.title} ({note.date.strftime('%Y.%m.%d')})\n\n{note.text}")

# Функция для редактирования заметки
def edit_note():
    index = int(input("Введите номер заметки для редактирования: "))
    title = input("Введите новый заголовок заметки: ")
    text = input("Введите новый текст заметки: ")
    date_input = input("Введите новую дату заметки в формате ГГГГ.ММ.ДД: ")
    date = datetime.datetime.strptime(date_input, "%Y.%m.%d").date()
    notes[index - 1] = Note(title, text, date)

# Функция для удаления заметки
def delete_note():
    index = int(input("Введите номер заметки для удаления: "))
    del notes[index - 1]

# Главная функция программы
def main():
    notes = load_notes()
    while True:
        print("1. Создать заметку")
        print("2. Список заметок")
        print("3. Выборка заметок по дате")
        print("4. Просмотреть заметку")
        print("5. Редактировать заметку")
        print("6. Удалить заметку")
        print("7. Выйти")
        choice = int(input("Введите номер выбранного действия: "))
        print()
        if choice == 1:
            note = create_note()
            notes.append(note)
            save_notes(notes)
            print("Заметка сохранена.\n")
        elif choice == 2:
            read_notes(notes)
            print()
        elif choice == 3:
            filtered_notes = filter_notes_by_date(notes)
            read_notes(filtered_notes)
            print()
        elif choice == 4:
            display_note()
            print()
        elif choice == 5:
            edit_note()
            save_notes(notes)
            print("Заметка отредактирована.\n")
        elif choice == 6:
            delete_note()
            save_notes(notes)
            print("Заметка удалена.\n")
        elif choice == 7:
            break

if __name__ == "__main__":
    main()
    