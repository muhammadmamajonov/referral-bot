import sqlite3
from datetime import datetime

class Database:
    def __init__(self, path_to_db="data/main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        data = None
        cursor.execute(sql, parameters)

        if commit:
            connection.commit()
        if fetchall:
            data = cursor.fetchall()
        if fetchone:
            data = cursor.fetchone()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE Users (
            id int NOT NULL,
            username varchar(100),
            full_name varchar(100),
            phone varchar(15),
            card_num varchar(20),
            address varchar(255),
            age int,
            language varchar(3),
            suggested int,
            earnings int DEFAULT 0,
            withdrawn_money int DEFAULT 0,
            gender varchar(10),
            PRIMARY KEY (id)
            );
        """
        self.execute(sql, commit=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, id: int, username: str, suggested: int=None, language: str = 'uz'):
        # SQL_EXAMPLE = "INSERT INTO Users(id) VALUES(1)"

        sql = """
        INSERT INTO Users(id, username, suggested, language) VALUES(?, ?, ?, ?)
        """
        self.execute(sql, parameters=(id, username, suggested, language), commit=True)
    
    def add_money_to_earnings(self, id):
        sql = f"Select earnings From Users Where id={id}"
        earnings = self.execute(sql, fetchone=True)[0]
        price = self.get_price_for_invited()
        total = earnings + price
        sql = f"Update Users SET earnings=?  where id=?"
        return self.execute(sql, parameters=(total, id), commit=True)

    def withdrawn(self, id, amount):
        sql = f"Select earnings, withdrawn_money From Users Where id={id}"
        money = self.execute(sql, fetchone=True)
        sql = f"Update Users SET earnings={money[0]-amount}, withdrawn_money={money[1]+amount} Where id={id}"
        return self.execute(sql, commit=True)

    def get_referer(self, user_id):
        sql = f"Select suggested From Users Where id={user_id}"
        referer_id = self.execute(sql, fetchone=True)
        print(referer_id)
        return referer_id[0]
        
    def set_click_number(self, id, click_number):
        sql = "UPDATE Users SET card_num=? WHERE id=?"
        self.execute(sql, parameters=(click_number, id), commit=True)

    def set_phone(self, id, phone):
        sql = "UPDATE Users SET phone=? WHERE id=?"
        self.execute(sql, parameters=(phone, id), commit=True)
        
    def set_language(self, id, language):
        sql = f"""
        UPDATE Users SET language=? WHERE id=?
        """
        return self.execute(sql, parameters=(language, id), commit=True)
    
    def set_age(self, id, age):
        sql = "UPDATE Users SET age=? WHERE id=?"
        return self.execute(sql, parameters=(age, id), commit=True)

    def set_address(self, id, address):
        sql = "UPDATE Users SET address=? WHERE id=?"
        return self.execute(sql, parameters=(address, id), commit=True)

    def get_language(self, id):
        sql = "SELECT language from Users where id=?"
        print(id, '>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> ID')
        result = self.execute(sql, parameters=(id,), fetchone=True)
        
        return result[0]

    def get_card_num(self, id):
        sql = "SELECT card_num from Users where id=?" 
        result = self.execute(sql, parameters=(id,), fetchone=True)
        return result[0]

    def get_phone_num(self, id):
        sql = "SELECT phone from Users where id=?" 
        result = self.execute(sql, parameters=(id,), fetchone=True)
        return result[0]

    def edit_user(self, id, full_name, phone, address, gender):
        sql = f"""
        UPDATE Users SET full_name=?, phone=?, address=?, gender=? WHERE id=?
        """
        return self.execute(sql, parameters=(full_name, phone, address, gender, id), commit=True)

    def select_all_users(self):
        sql = """
        SELECT * FROM Users
        """
        return self.execute(sql, fetchall=True)

    def select_user(self, id):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 "
        sql = f"SELECT * FROM Users WHERE id={id}"

        return self.execute(sql, fetchone=True)

    def count_friends(self, id):
        sql = "SELECT COUNT(*) FROM Users Where suggested=?;"
        friends_count = self.execute(sql, parameters=(id,), fetchone=True)
        return friends_count[0]
        
    def count_users(self):
        return self.execute("SELECT COUNT(*) FROM Users;", fetchone=True)

    # def delete_users(self):
    #     self.execute("DELETE FROM Users WHERE TRUE", commit=True)


    def create_table_withdraws(self):
        sql = """
        CREATE TABLE Withdraws (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            callback_id varchar(50),
            user_id int references Users(id),
            to_whom varchar(100),
            amount int,
            card_num varchar(20),
            phone_num varchar(20),
            date_time datetime,
            withdrawn int DEFAULT 0
            );
        """
        self.execute(sql, commit=True)

    def add_withdraw(self, callback_id, user_id: str, to: str, amount: int, card_num: str=None, phone_num: str=None):
        # SQL_EXAMPLE = "INSERT INTO Users(id) VALUES(1)"
        dtime = datetime.now()
        dtime = f"{dtime.year}-{dtime.month}-{dtime.day} {dtime.hour}:{dtime.minute}"

        sql = """
        INSERT INTO Withdraws(callback_id, user_id, to_whom, card_num, phone_num, amount, date_time) VALUES(?, ?, ?, ?, ?, ?, ?)
        """
        return self.execute(sql, parameters=(callback_id, user_id, to, card_num, phone_num, amount, dtime), commit=True, fetchone=True)

    def select_all_withdraws(self):
        sql = """
        SELECT * FROM Withdraws
        """
        return self.execute(sql, fetchall=True)

    def select_withraw(self, callback_id):
        # SQL_EXAMPLE = "SELECT * FROM Users where id=1 "
        sql = f"SELECT * FROM Withdraws WHERE callback_id={callback_id}"

        return self.execute(sql, fetchone=True)
    
    def get_amount(self, callback_id):
        sql = f"Select amount From Withdraws where callback_id={callback_id}"
        return self.execute(sql, fetchone=True)[0]

    def get_user_id(self, callback_id):
        sql = f"Select user_id From Withdraws Where callback_id={callback_id}"
        return self.execute(sql, fetchone=True)[0]
        
    def set_withdrawn(self, callback_id):
        sql = f"""
        UPDATE Withdraws SET withdrawn=1 WHERE callback_id={callback_id}
        """
        return self.execute(sql, commit=True)

    def select_all_withdrawns(self):
        sql = "Select * From Withdraws Where withdrawn=1"
        return self.execute(sql, fetchall=True)

    def count_withdraws(self):
        return self.execute("SELECT COUNT(*) FROM Withdraws;", fetchone=True)

# ----------------------- Create Table rules ------------ #
    def create_table_rules(self):
        sql = """
        CREATE TABLE Rules (
            id int NOT NULL,
            rules_uz MEDIUMTEXT(1000),
            rules_en MEDIUMTEXT(1000),
            rules_ru MEDIUMTEXT(1000),
            PRIMARY KEY (id)
            );

        """
        self.execute(sql, commit=True)

    def get_rules(self):
        sql = f"SELECT * FROM Rules WHERE id=1"
        return self.execute(sql, fetchone=True)

    def set_rules_uz(self, rules_uz: str):
        sql = f"""
        UPDATE Rules SET rules_uz=? WHERE id=?
        """
        return self.execute(sql, parameters=(rules_uz, 1), commit=True)

    def set_rules_en(self, rules_en):
        sql = f"""
        UPDATE Rules SET rules_en=? WHERE id=?
        """
        return self.execute(sql, parameters=(rules_en, 1), commit=True)
    
    def set_rules_ru(self, rules_ru):
        sql = f"""
        UPDATE Rules SET rules_ru=? WHERE id=?
        """
        return self.execute(sql, parameters=(rules_ru, 1), commit=True)

# ----------------------- Create Table Channels ------------ #

    def create_table_channels(self):
        sql = """
        CREATE TABLE Channels(
            id int Not Null,
            name varchar(255),
            link varchar(255)
        );"""

        self.execute(sql, commit=True)

    def add_channel(self, name, channel_id, link):
        sql = """
        INSERT INTO Channels(name, id, link) VALUES(?, ?, ?)"""
        self.execute(sql, parameters=(name, channel_id, link), commit=True)
        
    def get_channels(self):
        sql = """
        SELECT * FROM Channels"""

        return self.execute(sql, fetchall=True)

    def delete_channel(self, channel_id):
        sql = f"DELETE FROM Channels WHERE id='{channel_id}'"
        self.execute(sql, commit=True)

    def create_table_other_settings(self):
        sql = """
        CREATE TABLE OtherSettings(
            id int Not Null,
            price_for_invited int,
            contact_number varchar(20)
            );"""
        return self.execute(sql, commit=True)

    def set_price_for_invited(self, price):
        sql = "UPDATE OtherSettings SET price_for_invited=? Where id=1"
        return self.execute(sql, parameters=(price,), commit=True)

    def set_contact_number(self, phone_number):
        sql = "UPDATE OtherSettings SET contact_number=? Where id=1"
        return self.execute(sql, parameters=(phone_number,), commit=True)

    def get_price_for_invited(self):
        sql = "Select price_for_invited From OtherSettings where id=?"
        price = self.execute(sql, parameters=(1,), fetchone=True)
        return price[0]
    
    def get_contact_number(self):
        sql = "Select contact_number From OtherSettings where id=?"
        contact_number = self.execute(sql, parameters=(1,), fetchone=True)
        print(contact_number, "Contact ---------------- Contact")
        return contact_number[0]

    # def create_table_tasks(self):
    #     sql = """
    #     CREATE TABLE Tasks(
    #         id int NOT NULL AUTO_INCREMENT,
    #         task_uz TEXT,
    #         task_en TEXT,
    #         task_ru TEXT,
    #     )"""
    #     return self.execute(sql=sql, commit=True)

    # def add_task(self, task_uz, task_en, task_ru):
    #     sql = "INSERT INTO Tasks(task_uz, task_en, task_ru) VALUES(?, ?, ?)"
    #     return self.execute(sql=sql, parameters=(task_uz, task_en, task_ru), commit=True)

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")