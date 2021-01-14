import DTO
import sqlite3


class _Logistics:
    def __init__(self, conn):
        self.conn = conn

    def insert(self, logistic):  # insert Logistic DTO
        self._conn.execute("""
            INSERT INTO logistics (id, name, count_sent, count_received) VALUES (?, ?, ?, ?)
        """, [logistic.id, logistic.name, logistic.count_sent, logistic.count_received])

    def find(self, logistic_id):  # retrieve Logistic DTO
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name FROM logistics WHERE id = ?
        """, [logistic_id])
        return DTO.logistic(*c.fetchone())


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""
               INSERT INTO students (id, location, demand, logistic) VALUES (?, ?, ?, ?)
           """, [clinic.id, clinic.location, clinic.demand, clinic.logistic])

    def find(self, clinic_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name FROM students WHERE id = ?
        """, [clinic_id])

        return DTO.Clinics(*c.fetchone())


class _Clinics:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, clinic):
        self._conn.execute("""
               INSERT INTO students (id, location, demand, logistic) VALUES (?, ?, ?, ?)
           """, [clinic.id, clinic.location, clinic.demand, clinic.logistic])

    def find(self, clinic_id):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name FROM students WHERE id = ?
        """, [clinic_id])

        return DTO.Clinics(*c.fetchone())


class _Suppliers:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, supplier):
        self._conn.execute("""
            INSERT INTO grades (id, name, logistic) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.logistic])

    def find(self, name):
        c = self._conn.cursor()
        c.execute("""
            SELECT id, name FROM students WHERE name = ?
        """, [name])

        return DTO.Suppliers(*c.fetchone())


class _Vaccines:
    def __init__(self, conn):
        self._conn = conn

    def insert(self, vaccine):
        self._conn.execute("""
        INSERT INTO vaccines (id, date, supplier, quantity) Values (?, ?, ?, ?) 
        """, [vaccine.id, vaccine.date, vaccine.supplier, vaccine.quantity])

    def find(self, vaccine_id):
        c = self._conn.cursor()
        c.execute("""
                    SELECT * FROM vaccines WHERE id = ?
                """, [vaccine_id])
        return DTO.vaccines(*c.fetchone())