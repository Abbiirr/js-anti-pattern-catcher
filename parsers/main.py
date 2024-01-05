import os
import re
import csv

def parse_log(log_file_path):
    parsed_data = []
    current_directory = ""
    current_file = ""

    prefix_to_trim = "F:\\#projects\\smp\\js-anti-pattern-catcher\\testFiles\\"

    with open(log_file_path, 'r') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()
            if line.startswith(prefix_to_trim):  # Check if line starts with the specified directory pattern
                current_directory = os.path.dirname(line)
                current_file = os.path.basename(line)
            else:
                match = re.match(r'\s*(\d+:\d+)\s+(error|warning)\s+(.*)\s+(.*)', line)
                if match:
                    line_number = match.group(1)
                    error_type = match.group(2)
                    error_description = match.group(4)

                    trimmed_directory = current_directory.replace(prefix_to_trim, '')  # Trim prefix
                    parsed_data.append({
                        'directory_file_name': os.path.join(trimmed_directory, current_file),
                        'line_number': line_number,
                        'error_type': error_type,
                        'error_description': error_description
                    })

    return parsed_data


def export_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['directory_file_name', 'line_number', 'error_type', 'error_description']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in data:
            writer.writerow(entry)


# Example log file path
log_file_path = "F:\#projects\smp\js-anti-pattern-catcher\\bootstrap.log"

parsed_dataset = parse_log(log_file_path)

# Export the parsed dataset to a CSV file
output_csv_file = "bootstrap.csv"
export_to_csv(parsed_dataset, output_csv_file)
