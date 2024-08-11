import sqlite3
from datetime import datetime


class Logs:
    def __create_table(self):
        self.cur.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.name} (
                         time TEXT, 
                         type TEXT, 
                         message TEXT
                    )"""
        )
        self.con.commit()

    def __init__(self, name: str = "Logs", file: str = "logs.db"):
        self.name = name
        self.file = file
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.__create_table()

    def create_log(self, message: str, type: str = "INFO"):
        self.cur.execute(f"INSERT INTO {self.name} (time, type, message) VALUES(?, ?, ?)", (datetime.now().strftime('%Y.%m.%d  %H:%M:%S'), type, message))
        self.con.commit()

    def get_logs(self):
        self.cur.execute(f"SELECT time, type, message FROM {self.name}")
        mass = [f"[Log]: {el[0]} | [{el[1]}] | {el[2]}" for el in self.cur.fetchall()]
        return mass


if __name__ == '__main__':
    bd = Logs()
    bd.create_log("12345", )
    print(bd.get_logs())
