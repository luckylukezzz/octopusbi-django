import csv
import mysql.connector
import os

db_config = {
    'host': 'octopusbi-octopusdb.i.aivencloud.com',
    'port': 19423,
    'user': 'avnadmin',
    'password': 'AVNS__C9FKK7Q-EONQ87AQFi', 
    'database': 'defaultdb',
    'ssl_disabled': False,
   
}

csv_file_path = './csvs/student.csv'  
table_name = os.path.splitext(os.path.basename(csv_file_path))[0]


connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    columns = next(csv_reader)  

   
    create_table_query = f"""
    CREATE TABLE IF NOT EXISTS `{table_name}` (
        `{columns[0]}` INT PRIMARY KEY,
        `{columns[1]}` VARCHAR(255)
    );
    """
    cursor.execute(create_table_query)

    
    insert_query = f"INSERT INTO `{table_name}` ({', '.join(columns)}) VALUES (%s, %s)"

    for row in csv_reader:
        cursor.execute(insert_query, (int(row[0]), row[1]))
connection.commit()
cursor.close()
connection.close()

print(f"Data from {csv_file_path} has been successfully inserted into the {table_name} table.")
