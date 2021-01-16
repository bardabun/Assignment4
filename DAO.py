import DTO
import sqlite3


class Logistics:
    def __init__(self, dbcon):
        self._dbcon = dbcon

    def insert(self, logistic):  # insert Logistic DTO
        self._dbcon.execute("""
            INSERT INTO logistics (id, name, count_sent, count_received) VALUES (?, ?, ?, ?)
        """, [logistic.id, logistic.name, logistic.count_sent, logistic.count_received])

    def find(self, logistic):  # retrieve Logistic DTO
        c = self._dbcon.cursor()
        c.execute("""
            SELECT id, name FROM logistics WHERE id = ?
        """, [logistic])
        return DTO.Logistic(*c.fetchone())

    def update_count_received(self, supplier_name, quantity):
        self._dbcon.execute("""
        UPDATE logistics SET count_received = quantity WHERE name = supplier_name
        """)


class Clinics:
    def __init__(self, dbcon):
        self._dbcon = dbcon

    def insert(self, clinic):
        self._dbcon.execute("""
               INSERT INTO clinics (id, location, demand, logistic) VALUES (?, ?, ?, ?)
           """, [clinic.id, clinic.location, clinic.demand, clinic.logistic])

    def find(self, clinic_id):
        c = self._dbcon.cursor()
        c.execute("""
            SELECT id, name FROM clinics WHERE id = ?
        """, [clinic_id])

        return DTO.Clinics(*c.fetchone())

    def sub_demand(self, location, amount_received):
        self._dbcon.execute("""
                UPDATE clinics SET demand = ? WHERE location = ?
                """, [amount_received, location])


class Suppliers:
    def __init__(self, dbcon):
        self._dbcon = dbcon

    def insert(self, supplier):
        self._dbcon.execute("""
            INSERT INTO suppliers (id, name, logistic) VALUES (?, ?, ?)
        """, [supplier.id, supplier.name, supplier.logistic])

    def find(self, name):
        c = self._dbcon.cursor()
        c.execute("""
            SELECT id, name FROM suppliers WHERE name = ?""", [name])

        return DTO.Suppliers(*c.fetchone())


class Vaccines:
    def __init__(self, dbcon):
        self._dbcon = dbcon

    def insert(self, vaccine):
        self._dbcon.execute("""
        INSERT INTO vaccines (id, date, supplier, quantity) Values (?, ?, ?, ?)""",
                            [vaccine.id, vaccine.date, vaccine.supplier, vaccine.quantity])

    def find(self, vaccine_id):
        c = self._dbcon.cursor()
        c.execute("""
                    SELECT * FROM vaccines WHERE id = ?""", [vaccine_id])
        return DTO.Vaccines(*c.fetchone())

    def find_max_id(self):
        c = self._dbcon.cursor()
        c.execute("""SELECT MAX(id) FROM vaccines""")
        return c.fetchone()[0]
                        ##-----------------------------------------------------------------need to check [0]

    def delete_line(self, id_row):
        c = self._dbcon.cursor()
        c.execute("""DELETE FROM vaccines WHERE id = ?""", [id_row])
