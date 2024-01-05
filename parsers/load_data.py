import pandas as pd

# Load the CSV file into a pandas DataFrame
csv_file_path = "parsed_data.csv"
data = pd.read_csv(csv_file_path)

# Display summary statistics or information about the loaded data
print("Summary of the loaded data:")
print(data.info())  # Display information about the DataFrame
print("\nSample of the loaded data:")
print(data.head())  # Display the first few rows of the DataFrame
print("\nStatistical summary:")
print(data.describe())  # Display summary statistics (if applicable)
