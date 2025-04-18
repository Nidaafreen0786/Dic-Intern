import csv
import logging

def setup_logging():
    logging.basicConfig(filename='Employee.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logging.info("Starting data processing...")

def main():
    input_file_cities = 'C:/Users/nidab/Desktop/DIC INTERN NIDA/logging/cities.csv'
    input_file_states = 'C:/Users/nidab/Desktop/DIC INTERN NIDA/logging/states.csv'
    output_file = 'C:/Users/nidab/Desktop/DIC INTERN NIDA/logging/citystate.csv'
    
    setup_logging()

    try:
        states_data = read_csv(input_file_states, "states")
        cities_data = read_csv(input_file_cities, "cities")

        if states_data and cities_data:
            combined_data = combine_data(cities_data, states_data)
            write_csv(output_file, combined_data)
            logging.info(f"Combined data written to {output_file}")
            print(f"Combined data has been successfully written to {output_file}")
        else:
            return

    except FileNotFoundError as e:
        handle_file_not_found_error(e)

    except Exception as ex:
        handle_unexpected_error(ex)

def read_csv(file_name, data_type):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            data = list(csv.reader(file))
            logging.info(f"Read {len(data)} rows from {file_name}")
        return data
    except FileNotFoundError as e:
        logging.error(f"The file {file_name} does not exist. Please check the file name and try again.")
        return None
    except Exception as ex:
        logging.error(f"Error reading {data_type} data from {file_name}: {str(ex)}")
        return None

def combine_data(cities_data, states_data):
    combined_data = []
    for city_row, state_row in zip(cities_data, states_data):
        city_name = ', '.join(city_row).strip()
        state_name = ', '.join(state_row).strip()
        combined_data.append([city_name,state_name])
    return combined_data

def write_csv(file_name, data):
    try:
        with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
            csv.writer(csvfile).writerows(data)
            logging.info(f"Wrote {len(data)} rows to {file_name}")
    except Exception as ex:
        logging.error(f"Error writing combined data to {file_name}: {str(ex)}")

def handle_file_not_found_error(e):
    logging.error(f"The file {e.filename} does not exist. Please check the file name and try again.")
    print(f"The file {e.filename} does not exist. Please check the file name and try again.")

def handle_unexpected_error(ex):
    logging.error(f"Unexpected error : {str(ex)}")
    print("Please check the logs for details.")

if __name__ == "__main__":
    main()
