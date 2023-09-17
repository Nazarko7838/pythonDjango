import psycopg2


def create_connection():
    try:
        connection = psycopg2.connect(
            host='postgres',
            port='5432',
            database='postgres',
            user='postgres',
            password='root'
        )
        return connection
    except Exception as e:
        print("Error connecting to the database:", e)
        return None


conn = create_connection()
cursor = conn.cursor()
cursor.execute('CREATE TABLE IF NOT EXISTS datatable (data1 TEXT, data2 TEXT)')


def add_data(data_tuple):
    cursor.execute(f'INSERT INTO datatable VALUES {data_tuple}')
    conn.commit()
