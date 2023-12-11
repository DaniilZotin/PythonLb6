import mysql.connector

# Параметри підключення до бази даних
db_config = {
    'host': 'localhost',
    'port': 3307,  # Замініть на новий порт, який ви вказали у docker-compose.yml
    'user': 'daniil',
    'password': '1111',
    'database': 'shopmall',
}

# Створення підключення
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

# Створення бази даних
create_database_query = "CREATE DATABASE IF NOT EXISTS shopmall;"
cursor.execute(create_database_query)

select_database_query = "USE shopmall;"
cursor.execute(select_database_query)

delete_tables_query = "drop table if exists conversations, phones, clients, tariffs;"
cursor.execute(delete_tables_query)

create_tables = """
    CREATE TABLE IF NOT EXISTS clients (
    id_client INT AUTO_INCREMENT PRIMARY KEY,
    type_client VARCHAR(50),
    address VARCHAR(50),
    second_name VARCHAR(50),
    first_name VARCHAR(50),
    fathers_name VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS phones (
    phone_number VARCHAR(15) PRIMARY KEY,
    id_client INT,
    FOREIGN KEY (id_client) REFERENCES clients(id_client)
);

CREATE TABLE IF NOT EXISTS tariffs (
    id_tariff INT AUTO_INCREMENT PRIMARY KEY,
    call_type VARCHAR(50),
    cost_per_minute DECIMAL(10, 2)
);

CREATE TABLE IF NOT EXISTS conversations (
    id_conversation INT AUTO_INCREMENT PRIMARY KEY,
    conversation_date DATE,
    phone_number VARCHAR(15),
    minutes_spoken INT,
    id_tariff INT,
    FOREIGN KEY (phone_number) REFERENCES phones(phone_number),
    FOREIGN KEY (id_tariff) REFERENCES tariffs(id_tariff)
);
"""

insertions = """
INSERT INTO clients (type_client, address, second_name, first_name, fathers_name)
VALUES
    ('department', 'Address1', 'Smith', 'John', 'Robert'),
    ('individual', 'Address2', 'Johnson', 'Michael', 'James'),
    ('department', 'Address3', 'Williams', 'Mary', 'David'),
    ('individual', 'Address4', 'Brown', 'Jennifer', 'Elizabeth'),
    ('department', 'Address5', 'Davis', 'William', 'Richard'),
    ('individual', 'Address6', 'Garcia', 'Linda', 'Lorraine');

INSERT INTO phones (phone_number, id_client)
VALUES
    ('123-456-7890', 1),
    ('987-654-3210', 2),
    ('555-555-5555', 3),
    ('123-416-7891', 4),
    ('507-751-3310', 5),
    ('237-129-3010', 2),
    ('544-445-1554', 6);


INSERT INTO tariffs (call_type, cost_per_minute)
VALUES
    ('local', 0.10),
    ('international', 0.25),
    ('national', 0.15);  
     
INSERT INTO conversations (conversation_date, phone_number, minutes_spoken, id_tariff)
VALUES
    ('2023-12-05', '123-456-7890', 25, 1),
    ('2023-12-06', '987-654-3210', 12, 2),
    ('2023-12-07', '123-456-7890', 22, 1),
    ('2023-12-08', '555-555-5555', 10, 3),
    ('2023-12-09', '987-654-3210', 18, 2),
    ('2023-12-10', '123-456-7890', 30, 1),
    ('2023-12-11', '555-555-5555', 25, 3),
    ('2023-12-12', '987-654-3210', 20, 2),
    ('2023-12-13', '123-456-7890', 15, 1),
    ('2023-12-14', '555-555-5555', 14, 3),
    ('2023-12-15', '987-654-3210', 10, 2),
    ('2023-12-16', '123-456-7890', 28, 1),
    ('2023-12-17', '555-555-5555', 16, 3),
    ('2023-12-18', '987-654-3210', 22, 2),
    ('2023-12-20', '123-456-7890', 18, 1),
    ('2023-12-21', '987-654-3210', 25, 2),
    ('2023-12-22', '123-456-7890', 15, 1),
    ('2023-12-23', '555-555-5555', 20, 3),
    ('2023-12-24', '987-654-3210', 12, 2),
    ('2023-12-19', '123-456-7890', 17, 1);
"""

commands_create_tables = create_tables.split(';')

# Виконання кожної окремої команди
for command in commands_create_tables:
    if command.strip():
        cursor.execute(command)

conn.commit()

commands_insertions = insertions.split(';')
for insert in commands_insertions:
    if insert.strip():
        cursor.execute(insert)

# Скидання автоінкременту
reset_auto_increment_query = "ALTER TABLE clients AUTO_INCREMENT = 1"
cursor.execute(reset_auto_increment_query)
reset_auto_increment_query = "ALTER TABLE tariffs AUTO_INCREMENT = 1"
cursor.execute(reset_auto_increment_query)
reset_auto_increment_query = "ALTER TABLE conversations AUTO_INCREMENT = 1"
cursor.execute(reset_auto_increment_query)
reset_auto_increment_query = "ALTER TABLE phones AUTO_INCREMENT = 1"
cursor.execute(reset_auto_increment_query)

# Підтвердження змін
conn.commit()

# Закриття підключення
cursor.close()
conn.close()
