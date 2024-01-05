import os
import re
import csv

def parse_log(log_file_path):
    parsed_data = []

    with open(log_file_path, 'r') as file:
        lines = file.read().split('\n\n')

        for line in lines:
            if not line.strip():
                continue

            parts = line.split('\n')
            file_info = parts[0].split('  ')
            file_path = file_info[0].strip()
            file_directory = os.path.dirname(file_path)

            errors = parts[1:]

            for error in errors:
                match = re.match(r'\s*(\d+):(\d+)\s+(warning|error)\s+(.*)\s+(.*)', error)
                if match:
                    line_number = match.group(1)
                    column_number = match.group(2)
                    error_type = match.group(3)
                    error_message = match.group(4)
                    rule_name = match.group(5)

                    parsed_data.append({
                        'directory_file_name': os.path.join(file_directory, os.path.basename(file_path)),
                        'line_number': line_number,
                        'anti_pattern': rule_name
                    })

    return parsed_data


def export_to_csv(data, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['directory_file_name', 'line_number', 'anti_pattern']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in data:
            writer.writerow(entry)


# Example log file path
log_file_path = "F:\#projects\smp\js-anti-pattern-catcher\output.log"

parsed_dataset = parse_log(log_file_path)

# Export the parsed dataset to a CSV file
output_csv_file = "parsed_data.csv"
export_to_csv(parsed_dataset, output_csv_file)
