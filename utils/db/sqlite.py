import sqlite3


class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, parameters: tuple = None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters = ()
        connection = self.connection
        # connection.set_trace_callback(logger)
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
        '''
            oddiy foydalanuvchilar uchun jadvalni hosil qilish metodi
        '''
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
            telegram_id INTEGER NOT NULL,
            full_name VARCHAR(300),
            is_active BOOL DEFAULT 1,
            PRIMARY KEY (telegram_id)
            );
        """
        self.execute(sql, commit=True)


    def create_category_table(self):
        sql = """CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR(120)
        );"""
        self.execute(sql, commit=True)

    def create_products_table(self):
        sql = """CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nomi VARCHAR(255),
            category INTEGER
        )"""

    def add_default_categories(self):
        categories = ['Pitsa', 'Hot-dog', 'Burger', 'Sneklar']
        sql = """
            INSERT INTO category (name) VALUES (?)
        """
        for category in categories:
            self.execute(sql, parameters=(category, ), commit=True)
    
    def get_categories(self):
        sql = """SELECT id, name FROM category"""
        return self.execute(sql, fetchall=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ?" for item in parameters
        ])
        return sql, tuple(parameters.values())

    def add_user(self, telegram_id: int):
        sql = """
        INSERT OR IGNORE INTO Users(telegram_id) VALUES(?)
        """
        self.execute(sql, parameters=(telegram_id,), commit=True)

    def get_all_users(self):
        sql = '''SELECT telegram_id FROM Users WHERE is_active=1'''
        return self.execute(sql, fetchall=True)

# db = Database()
# db.create_category_table()
# db.add_default_categories()

def logger(statement):
    print(f"""
_____________________________________________________        
Executing: 
{statement}
_____________________________________________________
""")
