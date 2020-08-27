import tkinter as tk
from tkinter import messagebox
import sqlite3
from sqlite3 import Error

databaseName = 'TeamsDB.sqlite3'


def initial_setup_teams_table():
    conn = create_connection()

    sql_statement_drop_table = """ DROP TABLE teams;"""
    execute_sql(conn, sql_statement_drop_table)

    sql_statement_create_table = """ CREATE TABLE IF NOT EXISTS teams (
        teamNumber integer PRIMARY KEY,
        teamName text NOT NULL,
        score integer
    ); """
    execute_sql(conn, sql_statement_create_table)

    conn.close()


def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(databaseName)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn


def execute_sql(conn, sql_line):
    try:
        c = conn.cursor()
        c.execute(sql_line)
    except Error as e:
        print(e)


def add_to_teams(name):
    print()


def invalid_team_name_warning():
    messagebox.showinfo("Invalid Team Name",
                        "Team name must be greater than 1 character")


# returns True for a valid team name
# returns False for invalid team name
def validate_team_name(teamName):
    if len(teamName) <= 1:
        invalid_team_name_warning()
    else:
        add_to_teams(teamName)


def start_add_team_window():
    add_team_window = tk.Tk()
    add_team_window.title('Add a team...')
    add_team_window.maxsize(300, 200)
    add_team_window.minsize(300, 200)
    add_team_window.lift()
    add_team_window.attributes("-topmost", True)

    add_team_label = tk.Label(add_team_window, text='Enter team name:')
    add_team_label.place(x=10, y=70)

    add_team_entry = tk.Entry(add_team_window, width=30)
    add_team_entry.place(x=110, y=70)

    confirm_team_button = tk.Button(add_team_window, text='Confirm Team Name', width=25,
                                  command=lambda: validate_team_name(add_team_entry.get()))
    confirm_team_button.place(x=55, y=150)


def continue_game(window):
    window.destroy()



def new_game(window):
    window.destroy()
    initial_setup_teams_table()
    main_app_window()

def start():
    new_game_window = tk.Tk()
    new_game_window.title('New Game or Resume Game?')
    new_game_window.maxsize(400, 200)
    new_game_window.minsize(400, 200)

    new_game_prompt = tk.Label(new_game_window, text='Start a new game or continue existing game?')
    new_game_prompt.place(x=80, y=20)

    new_game_button = tk.Button(new_game_window, text='New Game', command=lambda: new_game(new_game_window))
    new_game_button.place(x=90, y=70)

    continue_button = tk.Button(new_game_window, text='Continue', command=lambda: continue_game(new_game_window))
    continue_button.place(x=240, y=70)

    restart_warning = tk.Label(new_game_window, text='Warning: starting new game will erase existing game!')
    restart_warning.place(x=56, y=160)

    new_game_window.mainloop()


def main_app_window():
    main_window = tk.Tk()
    main_window.title('Trivia Score Keeper')
    main_window.minsize(1280, 720)
    main_window.maxsize(1920, 1080)

    menu_bar = tk.Menu(main_window)
    main_window.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=False)
    file_menu.add_command(label="Add a Team", command=lambda: start_add_team_window())
    menu_bar.add_cascade(label="File", menu=file_menu)

    main_window.mainloop()


start()
