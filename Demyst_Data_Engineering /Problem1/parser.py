import os
import csv

def parse_fixed_width_to_csv(input_file, output_file, spec_file):
    with open(spec_file, "r", encoding="utf-8") as f:
        spec = eval(f.read())  # Use json module in production
    
    offsets = list(map(int, spec["Offsets"]))
    encoding = spec.get("FixedWidthEncoding", "utf-8")
    include_header = spec.get("IncludeHeader", "True") == "True"
    
    with open(input_file, "r", encoding=encoding) as infile, open(output_file, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.writer(outfile)

        if include_header:
            writer.writerow(spec["ColumnNames"])

        for line in infile:
            parsed_row = []
            start = 0
            for offset in offsets:
                parsed_row.append(line[start:start + offset].strip())
                start += offset
            writer.writerow(parsed_row)


if __name__ == "__main__":
    input_file = "input_file.txt"  
    output_file = "output.csv"     
    spec_file = "spec.json"  
    parse_fixed_width_to_csv(input_file, output_file, spec_file)