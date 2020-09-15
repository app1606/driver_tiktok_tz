import sqlite3
from fastapi import FastAPI
from datetime import datetime
import random

app = FastAPI(title="Landmark Operations")
DB_NAME = 'marks.db'

@app.get("/get"
        )
def get_all_landmarks():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""

        --sql 
        SELECT * FROM marks WHERE status = 1 
        ;

        """)
        landmarks_dict = {i: {'longitude': rec[2], 'latitude': rec[1]} for i, rec in enumerate(cursor)}
        conn.commit()
        conn.close()
        return {'detail': landmarks_dict
                }

@app.get("/add"
        )
def add_landmark(long: float, lat: float):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            --sql
            INSERT INTO marks (lat, long, mark_date, status) 
            VALUES(?,?,?,1)
            ;
        """,(lat, long, datetime.now().strftime('%c'),)
        )
        conn.commit()
        conn.close()
        return 

@app.get("/delete"
        )
def add_landmark(long: float, lat: float):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("""
            --sql
            UPDATE marks SET status = 0 
                WHERE lat = ? AND long = ?
            ;
        """,(lat, long, )
        )
        conn.commit()
        conn.close()
        return         

def main():
    def db_worker():
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.executescript("""
        --sql 
        PRAGMA foreign_keys = on
        ;

        --sql 
        CREATE TABLE IF NOT EXISTS marks
        (mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
        lat INTEGER,
        long INTEGER,
        mark_date TEXT,
        status INTEGER
        )
        ;
        """
        )
        cursor.execute("""
            --sql
            INSERT INTO marks (lat, long, mark_date, status) 
            VALUES(?,?,?,1)
            ;
        """,(random.uniform(-90,90), random.uniform(-90,90), datetime.now().strftime('%c'),)
        )
        conn.commit()
        conn.close()
    db_worker()

if __name__ == '__main__':
    main()
    