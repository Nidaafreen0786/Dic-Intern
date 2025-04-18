import mysql.connector
import logging
from config import mysql_host, mysql_user, mysql_password, mysql_database
import json

# Configure logging
logging.basicConfig(
    filename='database_operations.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

try:
    # Connecting to MySQL using config details
    logging.info('Connecting to MySQL')
    conn = mysql.connector.connect(
        host=mysql_host,
        user=mysql_user,
        password=mysql_password,
        database=mysql_database
    )
    cursor = conn.cursor()

    # Fetching all states for India (assuming country_id for India is 100001)
    logging.info('Fetching all states for India')
    cursor.execute('SELECT * FROM master_state_list WHERE country_id = 100001')
    india_states = cursor.fetchall()

    for state in india_states:
        state_id = state[0]
        state_name = state[1]

        logging.info(f"Fetching cities for state: {state_name} (ID: {state_id})")
        cursor.execute('SELECT * FROM master_city_list WHERE state_id = %s', (state_id,))
        state_cities = cursor.fetchall()

        # Writing state cities data to minified JSON file
        filename = f'{state_name.lower().replace(" ", "").replace(",", "").replace("-", "")}.json'
        with open(filename, 'w') as file:
            json.dump(state_cities, file, separators=(',', ':'))
            logging.info(f"Data written to {filename}")

    logging.info("All India state data processed successfully.")

except mysql.connector.Error as err:
    logging.error(f"MySQL Error: {err}")

except FileNotFoundError as fnf_err:
    logging.error(f"Config file not found: {fnf_err}")

finally:
    # Close connection
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        logging.info("MySQL connection is closed")