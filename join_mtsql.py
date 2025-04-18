import mysql.connector

try:
    # Connecting to MySQL Workbench
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nidaloop*23",
        database="student"
    )

    cursor = conn.cursor()

    # Perform SELECT queries to fetch existing data
    # Fetching all student_data records
    print("Fetching student_data data:")
    cursor.execute('''
        SELECT * FROM student_data
    ''')
    student_data_rows = cursor.fetchall()
    for row in student_data_rows:
        print(row)

    # Fetching all student_address records
    print("\nFetching student_address data:")
    cursor.execute('''
        SELECT * FROM student_address
    ''')
    student_address_rows = cursor.fetchall()
    for row in student_address_rows:
        print(row)

    # Fetch data using INNER JOIN
    print("\nFetching student_data with inner join on student_address:")
    cursor.execute('''
        SELECT *
        FROM student_data
        INNER JOIN student_address ON student_data.student_id=student_address.student_id 
    ''')
    result_rows = cursor.fetchall()
    for row in result_rows:
        print(row)

    # Fetch data using LEFT JOIN
    print("\nFetching student_data with left join on student_address:")
    cursor.execute('''
        SELECT *
        FROM student_data
        LEFT JOIN student_address ON student_data.student_id=student_address.student_id
    ''')
    result_rows = cursor.fetchall()
    for row in result_rows:
        print(row)

    # Fetch data using RIGHT JOIN
    print("\nFetching student_data with right join on student_address:")
    cursor.execute('''
         SELECT *
        FROM student_data
        RIGHT JOIN student_address ON student_data.student_id=student_address.student_id
    ''')
    result_rows = cursor.fetchall()
    for row in result_rows:
        print(row)

    # Fetch data using FULL JOIN (simulated with UNION of LEFT JOIN and RIGHT JOIN)
    print("\nFetching student_data with full join on student_address:")
    cursor.execute('''
         SELECT *
        FROM student_data
        LEFT JOIN student_address ON student_data.student_id=student_address.student_id
        UNION ALL
         SELECT *
        FROM student_data
        RIGHT JOIN student_address ON student_data.student_id=student_address.student_id
    ''')
    result_rows = cursor.fetchall()
    for row in result_rows:
        print(row)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close connection
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")