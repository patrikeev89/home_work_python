import tkinter as tk
from tkinter import messagebox
import sqlite3 as sq

# Функция для создания базы данных, если она не существует
def create_database():
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (id INTEGER PRIMARY KEY, name TEXT, phone TEXT, email TEXT, birthday TEXT, note TEXT)''')
    conn.commit()
    conn.close()

# Функция для добавления контакта
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    birthday = birthday_entry.get()
    note = note_entry.get()

    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("INSERT INTO contacts (name, phone, email, birthday, note) VALUES (?, ?, ?, ?, ?)", (name, phone, email, birthday, note))
    conn.commit()
    conn.close()

    messagebox.showinfo("Успех", "Контакт успешно добавлен")

# Функция для отображения всех контактов
def show_contacts():
    conn = sq.connect('phonebook.db')
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    conn.close()

    for contact in contacts:
        contact_listbox.insert(tk.END, contact)

# Создание базы данных, если она не существует
create_database()

# Создание основного окна
root = tk.Tk()
root.title("PhoneBook")

# Метки
tk.Label(root, text="Имя:").grid(row=0, column=0)
tk.Label(root, text="Телефон:").grid(row=1, column=0)
tk.Label(root, text="Электронная почта:").grid(row=2, column=0)
tk.Label(root, text="День рождения:").grid(row=3, column=0)
tk.Label(root, text="Заметка:").grid(row=4, column=0)

# Поля ввода
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)
phone_entry = tk.Entry(root)
phone_entry.grid(row=1, column=1)
email_entry = tk.Entry(root)
email_entry.grid(row=2, column=1)
birthday_entry = tk.Entry(root)
birthday_entry.grid(row=3, column=1)
note_entry = tk.Entry(root)
note_entry.grid(row=4, column=1)

# Кнопки
add_button = tk.Button(root, text="Добавить контакт", command=add_contact)
add_button.grid(row=5, column=0, columnspan=2, pady=10)
show_button = tk.Button(root, text="Показать контакты", command=show_contacts)
show_button.grid(row=6, column=0, columnspan=2, pady=10)

# Список для отображения контактов
contact_listbox = tk.Listbox(root)
contact_listbox.grid(row=7, column=0, columnspan=2)

root.mainloop()