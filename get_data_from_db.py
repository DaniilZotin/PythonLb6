import mysql.connector

# Параметри підключення до бази даних
db_config = {
    'host': 'localhost',
    'port': 3307,  # Замініть на новий порт, який ви вказали у docker-compose.yml
    'user': 'daniil',
    'password': '1111',
    'database': 'shopmall',
}

def execute_query(cursor, query):
    cursor.execute(query)
    result = cursor.fetchall()
    return result

def print_table(cursor, table_name):
    # Отримання структури таблиці
    desc_query = f"DESC {table_name};"
    structure = execute_query(cursor, desc_query)

    # Отримання даних з таблиці
    select_query = f"SELECT * FROM {table_name};"
    data = execute_query(cursor, select_query)

    # Виведення структури таблиці
    print(f"\nTable: {table_name}")
    print("Structure:")
    for column in structure:
        print(f"{column[0]:<20} {column[1]:<20}")

    # Виведення даних з таблиці
    print("\nData:")
    column_widths = [max(len(str(value)) for value in column) for column in zip(*data)]

    for row in data:
        formatted_row = " | ".join([f"{value}".ljust(width) for value, width in zip(row, column_widths)])
        print(formatted_row)

def main():
    # Створення підключення
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Отримання списку таблиць у базі даних
    show_tables_query = "SHOW TABLES;"
    tables = execute_query(cursor, show_tables_query)

    # Виведення структури та даних з кожної таблиці
    for table in tables:
        print_table(cursor, table[0])

    # Закриття підключення
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()