import pandas as pd

# Create Data with Duplicate data
student_details = {
    'ID': [213,314,423,423,754,754,665],
    'Name': ['Nida','Afreen','Beauty','Beauty','Golu','Golu','Gudiya'],
    'Age': [23, 22, 21, 21, 20, 20, 24],
    'Dept': ['MCA','Btech','BCA','BCA','BSc','BSc','MSc']
}
df = pd.DataFrame(student_details)

# Save the Data to a CSV file
csv_file_path = 'duplicate_data.csv'
df.to_csv(csv_file_path, index=False)

# Read CSV file
df_read = pd.read_csv(csv_file_path)

# Remove duplicate rows
df_no_duplicates = df_read.drop_duplicates()

# Save the cleaned Data to a new CSV file
clean_csv_file_path = 'clean_data.csv'
df_no_duplicates.to_csv(clean_csv_file_path, index=False)

# Display the original and cleaned Data
print("Original Data:")
print(df_read)
print("\nCleaned Data:")
print(df_no_duplicates)