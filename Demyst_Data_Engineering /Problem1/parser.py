import os
import csv
import json

# Function to parse a fixed-width file into a CSV file based on a given specification.
def parse_fixed_width_to_csv(input_file, output_file, spec_file):
    # Read the specification file to get offsets, encoding, and header information.
    with open(spec_file, "r", encoding="utf-8") as f:
        spec = json.load(f)

    offsets = list(map(int, spec["Offsets"]))  # Convert offsets to integers.
    encoding = spec.get("FixedWidthEncoding", "utf-8")  # Default to UTF-8 if not specified.
    include_header = spec.get("IncludeHeader", "True") == "True"  # Check if the header is included.

    # Open the input fixed-width file and output CSV file.
    with open(input_file, "r", encoding=encoding) as infile, open(output_file, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile)

        # Write header row if specified in the spec file.
        if include_header:
            writer.writerow(spec["ColumnNames"])

        # Parse each line in the input file according to the offsets.
        for line in infile:
            parsed_row = []
            start = 0
            for offset in offsets:
                parsed_row.append(line[start:start + offset].strip())  # Extract and strip each field.
                start += offset
            writer.writerow(parsed_row)  # Write the parsed row to the output CSV.

# Main script entry point.
if __name__ == "__main__":
    input_file = "input_file.txt"  # Path to the input fixed-width file.
    output_file = "output.csv"  # Path to the output CSV file.
    spec_file = "spec.json"  # Path to the specification file.
    parse_fixed_width_to_csv(input_file, output_file, spec_file)
