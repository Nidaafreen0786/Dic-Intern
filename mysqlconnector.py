import mysql.connector
import logging
import json
import re
from config import mysql_host, mysql_user, mysql_password, mysql_database

class DatabaseOperations:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.conn = None
        self.cursor = None
        self.configure_logging()
        self.connect()

    def configure_logging(self):
        logging.basicConfig(
            filename='database_operations.log',
            level=logging.INFO,
            format='%(asctime)s:%(levelname)s:%(message)s'
        )

    def connect(self):
        try:
            logging.info('Connecting to MySQL')
            self.conn = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.conn.cursor()
        except mysql.connector.Error as err:
            logging.error(f"MySQL Error: {err}")
            raise

    def sanitize_filename(self, name):
        return re.sub(r'[^a-zA-Z0-9]', '', name.lower())

    def fetch_states(self, country_id):
        try:
            logging.info(f'Fetching all states for country ID: {country_id}')
            self.cursor.execute('SELECT * FROM master_state_list WHERE country_id = %s', (country_id,))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            logging.error(f"MySQL Error: {err}")
            raise

    def fetch_cities(self, state_id):
        try:
            logging.info(f"Fetching cities for state ID: {state_id}")
            self.cursor.execute('SELECT * FROM master_city_list WHERE state_id = %s', (state_id,))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            logging.error(f"MySQL Error: {err}")
            raise

    def write_to_file(self, filename, data):
        try:
            with open(filename, 'w') as file:
                json.dump(data, file, separators=(',', ':'))
                logging.info(f"Data written to {filename}")
        except IOError as e:
            logging.error(f"File I/O Error: {e}")
            raise

    def process_data(self, country_id):
        try:
            states = self.fetch_states(country_id)
            for state in states:
                state_id = state[0]
                state_name = state[1]

                cities = self.fetch_cities(state_id)
                if cities:
                    filename = f'{self.sanitize_filename(state_name)}.json'
                    self.write_to_file(filename, cities)
                else:
                    logging.info(f"No cities found for state: {state_name} (ID: {state_id})")

            logging.info("All data processed successfully.")
        except Exception as e:
            logging.error(f"Error during data processing: {e}")
            raise

    def close_connection(self):
        if self.conn and self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            logging.info("MySQL connection is closed")

if __name__ == "__main__":
    try:
        db_ops = DatabaseOperations(mysql_host, mysql_user, mysql_password, mysql_database)
        db_ops.process_data(country_id=100001)  # Assuming 100001 is the country_id for India
    except Exception as e:
        logging.error(f"Unhandled error: {e}")
    finally:
        db_ops.close_connection()
