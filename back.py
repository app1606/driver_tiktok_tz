'''
back-end main file
'''
import sqlite3
from fastapi import FastAPI, Response
from datetime import datetime
import random

app = FastAPI(title='Landmark Operations')
DB_NAME = 'marks.db'


@app.get('/get')
def get_all_landmarks(response: Response):
    '''
    gets all landmarks from db and returns them

    Parameters
    ----------
    response : Response

    Returns
    -------
    dict
        format of the output
        {
            'detail': i: {
                'longitude': long as float,
                'lat': lat as float
            }
        }

    '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    --sql
    SELECT long, lat FROM marks WHERE status = 1
    ;
    ''')
    landmarks_dict = {
        i + 1: {
            'longitude': rec[0],
            'latitude': rec[1]
            } for i, rec in enumerate(cursor)}
    conn.commit()
    conn.close()
    response.headers['Access-Control-Allow-Origin'] = '*'
    return {'detail': landmarks_dict}


@app.get('/add')
def add_landmark(long: float, lat: float):
    '''
    adds landmark to the database with latitude and longitude given

    Parameters
    ----------
    long : float
        longitude
    lat : float
        latitude
    '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    --sql
    INSERT INTO marks (lat, long, mark_date, status)
    VALUES (?, ?, ?, 1)
    ;
    ''', (lat, long, datetime.now().strftime('%c'),))
    conn.commit()
    conn.close()
    return True


@app.get('/delete')
def delete_landmark(long: float, lat: float):
    '''
    deletes landmark from the database with latitude and longitude given
    delete means setting status to 0

    Parameters
    ----------
    long : float
        longitude
    lat : float
        latitude
    '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
    --sql
    UPDATE marks SET status = 0
        WHERE lat = ? AND long = ?
    ;
    ''', (lat, long,))
    conn.commit()
    conn.close()
    return True


def main():
    def db_worker():
        '''
        creates tables if they're not exists
        and puts random marks there
        '''
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.executescript('''
        --sql
        CREATE TABLE IF NOT EXISTS marks
        (mark_id INTEGER PRIMARY KEY AUTOINCREMENT,
        lat INTEGER,
        long INTEGER,
        mark_date TEXT,
        status INTEGER
        )
        ;
        ''')
        cursor.execute('''
            --sql
            INSERT INTO marks (lat, long, mark_date, status)
            VALUES (?, ?, ?, 1)
            ;
        ''', (random.uniform(-90, 90),
              random.uniform(-90, 90),
              datetime.now().strftime('%c'),)
        )
        conn.commit()
        conn.close()
    db_worker()


if __name__ == '__main__':
    main()
