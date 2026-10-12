import sqlite3


class CountryDatabaseManager:

    def __init__(self):
        self.conn = sqlite3.connect(
        "countries.db",
        check_same_thread=False
    )

        self.cursor = self.conn.cursor()

        self.create_table()

    def create_table(self):

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS countries(
            name TEXT PRIMARY KEY,
            capital TEXT,
            population INTEGER,
            area REAL
        )
        """)

        self.conn.commit()

    # ADD HERE ↓↓↓

    def insert_country(self, country):

        self.cursor.execute("""
        INSERT OR REPLACE INTO countries
        VALUES (?, ?, ?, ?)
        """,
        (
            country["name"],
            country["capital"],
            country["population"],
            country["area"]
        ))

        self.conn.commit()

    def get_all_countries(self):

        self.cursor.execute(
            "SELECT * FROM countries"
        )

        return self.cursor.fetchall()

    def get_country(self, name):

        self.cursor.execute(
            "SELECT * FROM countries WHERE name=?",
            (name,)
        )

        return self.cursor.fetchone()

    def update_country(self, name, capital, population, area):

        self.cursor.execute("""
        UPDATE countries
        SET capital=?,
            population=?,
            area=?
        WHERE name=?
        """,
        (
            capital,
            population,
            area,
            name
        ))

        self.conn.commit()

    def delete_country(self, name):

        self.cursor.execute(
            "DELETE FROM countries WHERE name=?",
            (name,)
        )

        self.conn.commit()
