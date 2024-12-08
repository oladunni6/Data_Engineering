import unittest
import os
from data_generator import generate_csv
from anon import anonymize_csv

class TestAnonymizer(unittest.TestCase):
    def setUp(self):
        self.raw_csv = "test_raw.csv"
        self.anonymized_csv = "test_anonymized.csv"

        # Generate test CSV file
        generate_csv(self.raw_csv, 10)  # Small dataset for testing

    def tearDown(self):
        os.remove(self.raw_csv)
        if os.path.exists(self.anonymized_csv):
            os.remove(self.anonymized_csv)

    def test_anonymization(self):
        anonymize_csv(self.raw_csv, self.anonymized_csv)
        self.assertTrue(os.path.exists(self.anonymized_csv))

        # Check if anonymized file is correctly processed
        with open(self.anonymized_csv + "/part-00000-*.csv", "r", encoding="utf-8") as f:
            header = f.readline().strip()
            self.assertEqual(header, "first_name,last_name,address,date_of_birth")

if __name__ == "__main__":
    unittest.main()