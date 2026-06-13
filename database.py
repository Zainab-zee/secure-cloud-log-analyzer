import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        return None

    return psycopg2.connect(database_url)


def create_table():

    conn = get_connection()

    if conn is None:
        return

    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS log_results(
            id SERIAL PRIMARY KEY,
            result_key VARCHAR(100),
            result_value INTEGER
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


def save_results(results):

    conn = get_connection()

    if conn is None:
        return

    cur = conn.cursor()

    for key, value in results.items():

        cur.execute(
            """
            INSERT INTO log_results
            (result_key, result_value)
            VALUES (%s, %s)
            """,
            (key, value)
        )

    conn.commit()

    cur.close()
    conn.close()