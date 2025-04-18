import mysql.connector
import json
import logging

# Configure logging
logging.basicConfig(
    filename='database_operations.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

try:
    # Connecting to MySQL Workbench
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Nidaloop*23",
        database="test_data"
    )

    cursor = conn.cursor()
    # Perform SELECT queries to fetch existing data
    # Fetching all master_city_list records
    logging.info('Fetching master_city_list data')
    cursor.execute('''
        SELECT * FROM master_city_list
    ''')
    
    master_city_list_rows = cursor.fetchall()
    for row in master_city_list_rows:
     logging.debug(f"master_city_list row: {row}")


    # Fetching all master_country_list records
    logging.info('Fetching master_country_list data')
    cursor.execute('''
        SELECT * FROM master_country_list
    ''')
    master_country_list_rows = cursor.fetchall()
    for row in master_country_list_rows:
        logging.debug(f"master_country_list row: {row}")

    # Fetching all master_state_list records
    logging.info('Fetching master_state_list data')
    cursor.execute('''
        SELECT * FROM master_state_list
    ''')
    master_state_list_rows = cursor.fetchall()
    for row in master_state_list_rows:
         logging.debug(f"master_state_list row: {row}")

    

    #Fetching all states for India
    logging.info('Fetching all states for India')
    cursor.execute('''
        SELECT *
        FROM master_state_list WHERE country_id = 100001;
    ''')
    india_states = cursor.fetchall()

    india_data = {}  

    for state in india_states:
        state_id = state[0]
        state_name = state[1]
        
        logging.info(f"Fetching cities for state: {state_name} (ID: {state_id})")
        cursor.execute('''
            SELECT * FROM master_city_list WHERE state_id = %s
        ''', (state_id,))
        state_cities = cursor.fetchall()

        india_data[state_name] = state_cities

        with open(f'{state_name}.json', 'w') as file:
            json.dump(state_cities, file, indent=4)
            logging.info(f"Data written to {state_name}.json")

    # All India data to JSON file
    with open('India_all_data.json', 'w') as file:
        json.dump(india_data, file, indent=4)
        logging.info("All India data written to India_all_data.json")

    print("Data written to JSON files successfully.")



except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close connection
    if 'conn' in locals() and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")
