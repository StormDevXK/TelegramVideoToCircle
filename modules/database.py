import sqlite3


class Users:
    def __create_table(self):
        self.cur.execute(
            f"""CREATE TABLE IF NOT EXISTS {self.name} (
                         id TEXT, 
                         free_trial INTEGER, 
                         paid_attempts INTEGER
                    )"""
        )
        self.con.commit()

    def __init__(self, name: str = "Users", file: str = "base.db"):
        self.name = name
        self.file = file
        self.con = sqlite3.connect(file)
        self.cur = self.con.cursor()
        self.__create_table()

    def create_user(self, id: str, free_trial: int, paid_attempts: int):
        if not self.is_user_in_db(id):
            self.cur.execute(f"INSERT INTO {self.name} VALUES({id}, {free_trial}, {paid_attempts})")

    def is_user_in_db(self, id: str):
        self.cur.execute(f"SELECT count(*) FROM {self.name} WHERE id = {id}")
        is_here = self.cur.fetchone()[0]
        if is_here == 0:
            return False
        else:
            return True

    def get_user(self, id: str):
        if self.is_user_in_db(id):
            self.cur.execute(f"SELECT link FROM {self.name} WHERE id = ?", (id,))
            a = []
            for result in self.cur.fetchall():
                a.append(result[0])
            return a


if __name__ == '__main__':
    bd = Users()
    bd.create_user("1234", 1, 0)