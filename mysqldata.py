import mysql.connector
from mysql.connector import Error

def create_table():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Nidaloop*23',
            database='nida_table'
        )

        if connection.is_connected():
            print("Connected to MySQL database for table creation")

            cursor = connection.cursor()

            # Create table query
            create_table_query = '''
            CREATE TABLE IF NOT EXISTS nida_intern (id INT,name VARCHAR(55) NOT NULL,age INT NOT NULL,dept VARCHAR(50) NOT NULL)'''
            cursor.execute(create_table_query)

            # Insert mysql data
            insert_data_query = '''
            INSERT INTO nida_intern (id, name, age, dept) VALUES (%s, %s, %s, %s)'''
            nida_data = [(240, 'nida', 23, 'mca'),(4578, 'afreen', 23, 'mca'),(568, 'sneha', 22, 'btech')]

            cursor.executemany(insert_data_query, nida_data)
            connection.commit()

            print("Table created and sample data inserted successfully")

    except Error as e:
        print(f"Error: {e}")

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

create_table()