import sqlite3
from config import Config


def get_db_connection():

    conn = sqlite3.connect(
        Config.DATABASE,
        timeout=30
    )

    conn.row_factory = sqlite3.Row

    return conn