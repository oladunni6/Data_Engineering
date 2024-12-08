import csv
from faker import Faker

fake = Faker()

def generate_csv(file_path, num_records):
    with open(file_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["first_name", "last_name", "address", "date_of_birth"])
        for _ in range(num_records):
            writer.writerow([
                fake.first_name(),
                fake.last_name(),
                fake.address(),
                fake.date_of_birth().isoformat()
            ])