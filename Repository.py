import sqlite3
import atexit
import os

# The Repository
import DAO
import DTO

os.path.isfile('config.txt')


class Repository:
    def __init__(self):
        myfile = 'database.db'
        if os.path.isfile(myfile):
            os.remove(myfile)
        self._dbcon = sqlite3.connect('database.db')
        self.vaccines = DAO.Vaccines(self._dbcon)
        self.clinics = DAO.Clinics(self._dbcon)
        self.suppliers = DAO.Suppliers(self._dbcon)
        self.logistics = DAO.Logistics(self._dbcon)

    def read_insert(self, config_file):
        with open(config_file) as f:
            f = f.readlines()  # f stands for file -- make my file list
        config_first_line = f[0]
        config_first_line = config_first_line[:-1]
        split_config_first_line = config_first_line.split(",")

        list_entries_vaccines = []
        list_entries_suppliers = []
        list_entries_clinics = []
        list_entries_logistics = []
        lines_to_read_vac = int(split_config_first_line[0])
        lines_to_read_sup = int(split_config_first_line[1])
        lines_to_read_clin = int(split_config_first_line[2])
        lines_to_read_log = int(split_config_first_line[3])
        range1 = range(1, 1 + lines_to_read_vac)
        range2 = range(1 + lines_to_read_vac, lines_to_read_sup + 1 + lines_to_read_vac)
        range3 = range(lines_to_read_sup + 1 + lines_to_read_vac,
                       lines_to_read_sup + 1 + lines_to_read_vac + lines_to_read_clin)
        range4 = range(lines_to_read_sup + 1 + lines_to_read_vac + lines_to_read_clin,
                       lines_to_read_sup + 1 + lines_to_read_vac + lines_to_read_clin + lines_to_read_log)

        for i in range1:
            list_entries_vaccines = f[i]
        for i in range2:
            list_entries_suppliers = f[i]
        for i in range3:
            list_entries_clinics = f[i]
        for i in range4:
            list_entries_logistics = f[i]

        for i in list_entries_vaccines:
            i = i[:-1]
        i = i.split(',')
        vaccine = DTO.Vaccines(*i)
        insert_vac = DAO.Vaccines(self._dbcon)
        insert_vac.insert(vaccine)

        for i in list_entries_suppliers:
            i = i[:-1]
        i = i.split(',')
        supplier = DTO.Suppliers(*i)
        insert_sup = DAO.Suppliers(self._dbcon)
        insert_sup.insert(supplier)

        for i in list_entries_clinics:
            i = i[:-1]
        i = i.split(',')
        clinic = DTO.Clinics(*i)
        insert_cli = DAO.Clinics(self._dbcon)
        insert_cli.insert(clinic)

        for i in list_entries_logistics:
            i = i[:-1]
        i = i.split(',')
        logistic = DTO.Logistic(*i)
        insert_log = DAO.Logistics(self._dbcon)
        insert_log.insert(logistic)

    def _close(self):
        self._dbcon.commit()

    def create_tables(self):
        self._dbcon.executescript("""
                CREATE TABLE vaccines (
                    id           INT         PRIMARY KEY,
                    date        STRING        NOT NULL,
                    supplier     INT        REFERENCES supplier(id),
                    quantity     INT           NOT NULL
                ); 

                CREATE TABLE suppliers (
                    id        INT     PRIMARY KEY,
                    name     STRING    NOT NULL,
                    logistic  INT      REFERENCES logistic(id)
                );

                CREATE TABLE clinics (
                    id      INT         PRIMARY KEY,
                    location    STRING     NOT NULL,
                    demand      INT        NOT NULL,
                    logistic    INT     REFERENCES logistic(id)
                );

                CREATE TABLE logistics (
                    id              INT     PRIMARY KEY,
                    name          STRING    NOT NULL,
                    count_sent      INT     NOT NULL,
                    count_received  INT     NOT NULL
                );
            """)







# the repository singleton
repo = Repository()
atexit.register(repo._close)
