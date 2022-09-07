import sqlite3
from db_config import DATABASE_FILENAME
from os.path import exists


def execute(command):
    with sqlite3.connect(DATABASE_FILENAME) as con:
        return con.execute(command)

def select(column, table):
    command = f'SELECT {column} FROM {table};'
    return execute(command).fetchall()


def show():
    entries = select("*", "entry")
    for entry in entries:
        print(entry)

def insert(table, columns, values):
    command = f'INSERT INTO {table} ({columns}) VALUES ({values});'
    execute(command)

def add():
    day = input("What is your main goal today?: ")
    week = input("What is your main goal this week?: ")
    month = input("What is your main goal this month?: ")
    year = input("What is your main goal this year?: ")
    insert("entry", "goal_day, goal_week, goal_month, goal_year, entry_date", f'"{day}", "{week}", "{month}", "{year}", DATE("now")')

stop = False
def quit():
    global stop
    stop = True


def menu():
    options = [{"label": "List all previous entries", "action": show}, {"label": "Add an entry", "action": add}, {"label": "Quit", "action": quit}]
    print("What would you like to do?")
    for i in range(0, len(options)):
        option = options[i]
        print(f"[{i}] {option['label']}")
    selection = int(input(">>> "))
    if selection > len(options)-1 or selection < 0:
        print("Not an option")
    else:
        options[selection]["action"]()
if not exists(DATABASE_FILENAME):
    import init_db
while not stop:
    menu()
