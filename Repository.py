import sqlite3
import atexit
import os

# The Repository
from DTO import *
os.path.isfile('config.txt')


class _Repository:
    def __init__(self):
        myfile = 'database.db'
        if os.path.isfile(myfile):
            os.remove(myfile)
        self._conn = sqlite3.connect('database.db')
        self.vaccines = Vaccines(self.conn)
        self.clinics = Clinics(self.conn)
        self.grades = Grades(self.conn)
        self.logistics = Logistics(self.conn)

    def _close(self):
        self._conn.commit()
        self._conn.close()

    def create_tables(self):
        self._conn.executescript("""
        CREATE TABLE vaccines (
            id      INT         PRIMARY KEY,
            date    STRING        NOT NULL
            supplier INT REFERENCES supplier(id),
            quantity INT NOT NULL
        );

        CREATE TABLE suppliers (
            id                 INT     PRIMARY KEY,
            name     STRING    NOT NULL,
            logistic INT REFERENCES logistic(id),
        );

        CREATE TABLE clinics (
            id      INT         PRIMARY KEY,
            location    STRING     NOT NULL
            demand      INT        NOT NULL,
            logistic INT REFERENCES logistic(id),
        );
        
        CREATE TABLE logistics (
            id              INT     PRIMARY KEY,
            name          STRING    NOT NULL
            count_sent      INT     NOT NULL,
            count_received  INT     NOT NULL,
        );
    """)


# the repository singleton
repo = _Repository()
atexit.register(repo._close)