from flask import Flask, render_template, request
import pymysql
app = Flask(__name__)

# Database configuration
DB_HOST = "mysql_test-database-1"
DB_PORT = 3306
DB_NAME = "default"
DB_USER = "root"
DB_PASSWORD = "root"

def create_connection():
    try:
        connection = pymysql.connect(
            host=DB_HOST,
            port=DB_PORT,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
        )
        return connection
    except Exception as e:
        return f"Error connecting to the database: {e}"


@app.route('/')
def home():
    connection = create_connection()
    if type(connection) != str:
        return "Connected to MySQL database!"
    else:
        return f"Failed to connect to MySQL database. {connection}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)



# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # Функція для додавання даних до бази даних
# def add_data(data):
#     conn = sqlite3.connect('database.db')
#     c = conn.cursor()
#     c.execute('CREATE TABLE IF NOT EXISTS data_table (data TEXT)')
#     c.execute('INSERT INTO data_table (data) VALUES (?)', (data,))
#     conn.commit()
#     conn.close()
#
# # Роут для обробки введених даних та запису в базу даних
# @app.route('/process_data', methods=['POST'])
# def process_data():
#     data = request.form.get('data')  # Отримуємо дані з поля вводу з форми
#
#     # Перевіряємо, чи отримали дані перед записом
#     if data:
#         add_data(data)
#         return f'Data "{data}" has been saved to the database.'
#     else:
#         return 'No data received. Please enter some data.'
#
#
#
#
#




# @app.route('/')
# def index():
#     return render_template('index.html')
#
# # Роут для обробки введених даних та запису в базу даних
# @app.route('/process_data', methods=['POST'])
# def process_data():
#     if request.method == 'POST':
#         add_data(data)
#         return f'Data "{data}" has been saved to the database.'











# if __name__ == "__main__":
#     app.run(host="0.0.0.0")

