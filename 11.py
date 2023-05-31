import json

# Класс, описывающий заметку
class Note:
    def __init__(self, title, text):
        self.title = title
        self.text = text

# Функция для создания заметки
def create_note():
    title = input("Введите заголовок заметки: ")
    text = input("Введите текст заметки: ")
    note = Note(title, text)
    return note

# Функция для сохранения заметок в файл
def save_notes(notes):
    with open("notes.json", "w") as f:
        json.dump(notes, f, indent=4)

# Функция для загрузки заметок из файла
def load_notes():
    try:
        with open("notes.json", "r") as f:
            notes = json.load(f)
    except FileNotFoundError:
        notes = []
    return notes

# Функция для чтения списка заметок
def read_notes(notes):
    for index, note in enumerate(notes):
        print(f"{index + 1}. {note.title}")

# Функция для редактирования заметки
def edit_note():
    index = int(input("Введите номер заметки для редактирования: "))
    title = input("Введите новый заголовок заметки: ")
    text = input("Введите новый текст заметки: ")
    notes[index - 1] = Note(title, text)

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
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Выйти")
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
            edit_note()
            save_notes(notes)
            print("Заметка отредактирована.\n")
        elif choice == 4:
            delete_note()
            save_notes(notes)
            print("Заметка удалена.\n")
        elif choice == 5:
            break

if __name__ == "__main__":
    main()