from data_generator import generate_csv
from anon import anonymize_csv

if __name__ == "__main__":
    raw_csv = "raw_data.csv"
    anonymized_csv = "anonymized_data.csv"

    generate_csv(raw_csv, 10000)  # Generate 10,000 records
    anonymize_csv(raw_csv, anonymized_csv)