import sqlite3 as sq

# Создание базы данных, если она еще не существует
def create_database():
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, birthday TEXT, note TEXT)''')
    conn.commit()
    conn.close()

# Добавления контакта
def add_contact(name, phone, email=None, birthday=None, note=None):
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, phone, email, birthday, note) VALUES (?, ?, ?, ?, ?)", (name, phone, email, birthday, note))
    conn.commit()
    conn.close()

# Просмотр всех контактов
def all_contacts():
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    conn.close()
    return contacts

# Поиск контакта по имени
def search_contact(name):
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE name=?", (name,))
    contact = c.fetchone()
    conn.close()
    return contact

# Поиск контакта по номеру телефона
def search_contact_by_phone(phone):
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts WHERE phone=?", (phone,))
    contact = c.fetchone()
    conn.close()
    return contact

# Удаления контакта по имени
def delete_contact(name):
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("DELETE FROM contacts WHERE name=?", (name,))
    conn.commit()
    conn.close()

# Изменение номера телефона контакта по имени
def update_contact(name, new_phone):
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("UPDATE contacts SET phone=? WHERE name=?", (new_phone, name))
    conn.commit()
    conn.close()

# Изменение e-mail контакта по имени
def update_contact_email(name, new_email):
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("UPDATE contacts SET email=? WHERE name=?", (new_email, name))
    conn.commit()
    conn.close()

# Изменение даты рождения контакта по имени
def update_contact_birthday(name, new_birthday):
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("UPDATE contacts SET birthday=? WHERE name=?", (new_birthday, name))
    conn.commit()
    conn.close()

# Изменение текстовой заметки контакта по имени
def update_contact_note(name, new_note):
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("UPDATE contacts SET note=? WHERE name=?", (new_note, name))
    conn.commit()
    conn.close()

# Создаем базу данных, если её нет
create_database()

# Использование функций
# add_contact("Иванов Иван", "+79220010001")
# add_contact("Петров Петр", "+79220020002")
# add_contact("Сидоров Сидор", "+79220030003")

# print("Все контакты:")
# print(all_contacts())

# print("\nПоиск контакта 'Иванов Иван':")
# print(search_contact("Иванов Иван"))

# print("\nУдаление контакта 'Петров Петр':")
# delete_contact("Петров Петр")
# print(all_contacts())

# print("\nИзменение номера телефона для 'Сидоров Сидор':")
# update_contact("Сидоров Сидор", "+79220040004")
# print(all_contacts())

# print("\nПоиск контакта с номером телефона '+79220020002':")
# print(search_contact_by_phone("+79220020002"))

# print("\nИзменение e-mail для 'Сидоров Сидор':")
# update_contact_email("Сидоров Сидор", "sidorov_s@mail.ru")
# print(all_contacts())

# print("\nИзменение даты рождения для 'Петров Петр':")
# update_contact_birthday("Петров Петр", "1989-08-01")
# print(all_contacts())

# print("\nИзменение заметки для 'Иванов Иван':")
# update_contact_note("Иванов Иван", "Новая заметка")
# print(all_contacts())