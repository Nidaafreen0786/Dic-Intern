import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_log_file(file_path):
    """
    Reads the content of the specified log file.

    Args:
    file_path (str): The path to the log file to be read.

    Returns:
    str: The content of the log file.
    """
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        logging.error(f"The specified log file was not found: {file_path}")
        return "The specified log file was not found."
    except IOError as e:
        logging.error(f"An error occurred while reading the log file: {e}")
        return f"An error occurred while reading the log file: {e}"

def clear_log_file(file_path):
    """
    Clears the content of the specified log file.

    Args:
    file_path (str): The path to the log file to be cleared.
    """
    try:
        # Open the log file in write mode to truncate its content
        with open(file_path, 'w') as file:
            # Write nothing to the file to clear it
            file.write("")
        logging.info(f"The log file at {file_path} has been cleared.")
    except FileNotFoundError:
        logging.error(f"The specified log file was not found: {file_path}")
        # Create the file if it does not exist
        open(file_path, 'w').close()
        logging.info(f"The log file at {file_path} has been created.")
    except IOError as e:
        logging.error(f"An error occurred while clearing the log file: {e}")

# Specify the path to your log file
log_file_path = 'logs/logfile.log'

# Ensure the log directory exists
log_dir = os.path.dirname(log_file_path)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)
    logging.info(f"Created the directory {log_dir} for the log file.")

# Ensure the log file exists
if not os.path.exists(log_file_path):
    open(log_file_path, 'w').close()
    logging.info(f"Created the log file at {log_file_path}.")

# Read and print the content of the log file before clearing it
print("Log file content before clearing:")
print(read_log_file(log_file_path))

# Call the function to clear the log file
clear_log_file(log_file_path)

# Read and print the content of the log file after clearing it
print("\nLog file content after clearing:")
print(read_log_file(log_file_path))
