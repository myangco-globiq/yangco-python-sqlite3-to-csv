import sqlite3

def get_records(query):
    output = []
    db_conn = sqlite3.connect(r'db\yangcodb')
    cursor = db_conn.cursor()
    result = cursor.execute(query)
    output = result.fetchall()
    db_conn.close()

    return output