import sqlite3
import pygame
pygame.mixer.init()


def play():
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play(loops=0)


def connect():
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS game (id INTEGER PRIMARY KEY, title text, developer text, year integer, genre text)"
    )
    conn.commit()
    conn.close()


def insert(title, developer, year, genre):
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO game VALUES (NULL,?,?,?,?)", (title, developer, year, genre)
    )

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM game")
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def search(title="", developer="", year="", genre=""):
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM game WHERE title=? OR developer=? OR year=? OR genre=?",
        (title, developer, year, genre),
    )
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows


def delete(id):
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM game WHERE id=?", (id,))

    conn.commit()
    conn.close()


def update(id, title, developer, year, genre):
    conn = sqlite3.connect("games.db")
    cur = conn.cursor()

    cur.execute(
        "UPDATE game SET title=?, developer=?, year=?, genre=? WHERE id=?",
        (title, developer, year, genre, id),
    )

    conn.commit()
    conn.close()


connect()
