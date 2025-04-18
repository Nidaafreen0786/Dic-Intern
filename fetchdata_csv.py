import mysql.connector
import csv

def fetch_data():
    try:
        # Establishing the connection to MySQL
        conn = mysql.connector.connect(
            host='localhost',
            database='nida_table',
            user='root',
            password='Nidaloop*23'
        )

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM nida_intern")
            records = cursor.fetchall()

            # Saving the fetched data to a CSV file
            with open('nida.csv', 'w', newline='') as f:
                csv_writer = csv.writer(f)
                
                # Write headers
                csv_writer.writerow(['id', 'name', 'age', 'dept'])
                
                # Write data rows
                csv_writer.writerows(records)
                
            print("Data saved to nida.csv")

    except mysql.connector.Error as e:
        print(f"Error: {e}")

    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

fetch_data()