""" Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента. """

import json
from datetime import datetime

file_notes = 'notes.json'

def save_note(note):
    with open(file_notes, 'w') as file:
        json.dump(note, file, indent=4)

def read_note():
    try:
        with open(file_notes, 'r') as file:
            data = file.read()
            if not data:
                return []
            return json.loads(data)
    except FileNotFoundError:
        return []
    
def add_note():
    title = input('Введите заголовок заметки: ')
    text_note = input('Введите тело заметки: ')
    notes = read_note()
    note = {'id': len(notes) + 1, 'title': title, 'text': text_note, 'date': datetime.now().strftime('%d-%m-%Y %H:%M:%S')}
    notes.append(note)
    save_note(notes)
    print('Заметка успешно сохранена.')
    print(input('Для продолжения нажмите Enter: '))

def edit_note():
    note_id = int(input('Введите ID заметки для редактирования: '))
    notes = read_note()
    if not notes:
        print("Заметки отсутствуют")
        input('Для продолжения нажмите Enter: ')
        return
    for note in notes:
        if note['id'] == note_id:
            new_title = input('Введите новый заголовок заметки: ')
            new_text = input('Введите новое тело заметки: ')
            new_date = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
            if new_title:
                note['title'] = new_title
            if new_text:
                note['text'] = new_text
            if new_date:
                note['date'] = new_date
            save_note(notes)
            print('Заметка успешно отредактирована.')
            print(input('Для продолжения нажмите Enter: '))
            return
    print('Заметка с указанным ID не найдена')
    print(input('Для продолжения нажмите Enter: '))

def delete_note():
    note_id = int(input('Введите ID заметки для удаления: '))
    notes = read_note()
    if not notes:
        print("Заметки отсутствуют")
        input('Для продолжения нажмите Enter: ')
        return
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            save_note(notes)
            print('Заметка успешно удалена.')
            print(input('Для продолжения нажмите Enter: '))
            return
    print('Заметка с указанным ID не найдена')
    print(input('Для продолжения нажмите Enter: '))

def list_notes():
    print()
    notes = read_note()
    if not notes:
        print("Заметки отсутствуют")
        input('Для продолжения нажмите Enter: ')
        return
    for note in notes:
        print(f"ID: {note['id']}, Заголовок: {note['title']}, Тело заметки: {note['text']}, Дата/Время: {note['date']}")
    print(input('Для продолжения нажмите Enter: '))

def main():
    while True:
        print('\nДоступные команды: ')
        print('1. list - Просмотреть список заметок')
        print('2. add - Добавить заметку')
        print('3. edit - Редактировать заметку')
        print('4. delete - Удалить заметку')
        print('5. exit - Выйти из программы')

        command = input('Введите команду: ')
        if command == 'list' or command == '1':
            list_notes()
        elif command == 'add' or command == '2':
            add_note()
        elif command == 'edit' or command == '3':
            edit_note()
        elif command == 'delete' or command == '4':
            delete_note()
        elif command == 'exit' or command == '5':
            break
        else:
            print()
            print('Некорректная команда')
            print(input('Для продолжения нажмите Enter: '))

if __name__ == "__main__":
    main()