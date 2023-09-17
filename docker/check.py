from database import create_connection

conn = create_connection()
cur = conn.cursor()

print(cur.execute('SELECT * FROM database').fetchall())