import mysql.connector

try:
    # Connecting to MySQL Workbench
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nidaloop*23",
        database="nida_table"
    )
    cursor = conn.cursor()

    # Create table Employee
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS student ( id INT, name VARCHAR(255),age INT, dept VARCHAR(25))''')

    # Insert data into MySQL Employee
    cursor.execute('''INSERT INTO student (id, name, age, dept) VALUES (%s, %s, %s, %s)''', (44, 'Afreen', 22, 'Btech'))
    cursor.execute('''INSERT INTO student (id, name, age, dept) VALUES (%s, %s, %s, %s)''', (89, 'Golu', 30, 'MCA'))
    cursor.execute('''INSERT INTO student (id, name, age, dept) VALUES (%s, %s, %s, %s)''', (89, 'Beauty', 22, 'Btech'))

    # Commit the transaction
    conn.commit()

    # Read data from Employee
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    print("Read Operations:")
    for row in rows:
        print(row)

    # Update data in Employee
    cursor.execute("UPDATE student SET age = %s WHERE name = %s AND dept = %s", (23, 'Nida Afreen', 'MCA'))
    conn.commit()
    print("Update operation successful.")

    #Delete data from Employee
    cursor.execute("DELETE FROM student WHERE name = %s AND dept = %s", ('Beauty', 'Btech'))
    conn.commit()
    print("Delete operation successful.")
    
    # Read data again to verify changes
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    print("Read Operations after Update and Delete:")
    for row in rows:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if conn.is_connected():
        cursor.close()
        conn.close()