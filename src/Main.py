import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql


def create_connection():
    print()


def add_to_teams(name):
    print()


def invalid_team_name_warning():
    messagebox.showinfo("Invalid Team Name",
                        "Team name must be greater than 1 character")


#returns True for a valid team name
#returns False for invalid team name
def validate_team_name(teamName):
    if len(teamName) <= 1:
        invalid_team_name_warning()
    else:
        add_to_teams(teamName)


def add_team_window():
    addTeamWindow = tk.Tk()
    addTeamWindow.title('Add a team...')
    addTeamWindow.maxsize(300, 200)
    addTeamWindow.minsize(300, 200)
    addTeamWindow.lift()
    addTeamWindow.attributes("-topmost", True)

    addTeamLabel = tk.Label(addTeamWindow, text='Enter team name:')
    addTeamLabel.place(x=10, y=70)

    addTeamEntry = tk.Entry(addTeamWindow, width=30)
    addTeamEntry.place(x=110, y=70)

    confirmTeamButton = tk.Button(addTeamWindow, text='Confirm Team Name', width=25,
                                  command=lambda: validate_team_name(addTeamEntry.get()))
    confirmTeamButton.place(x=55, y=150)

window = tk.Tk()
window.title('Trivia Score Keeper')
window.minsize(1280, 720)
window.maxsize(1920, 1080)
addTeamButton = tk.Button(window, text='Add a Team', width=25, command=add_team_window)
addTeamButton.place(x=0, y=0)
window.mainloop()
