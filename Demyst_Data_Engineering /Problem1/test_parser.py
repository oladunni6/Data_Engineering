import unittest
import os
from parser import parse_fixed_width_to_csv

class TestParser(unittest.TestCase):
    def setUp(self):
        self.input_file = "test_input.txt"
        self.output_file = "test_output.csv"
        self.spec_file = "spec.json"

        with open(self.spec_file, "w", encoding="utf-8") as spec:
            spec.write(json.dumps({
                "ColumnNames": ["f1", "f2", "f3"],
                "Offsets": [5, 5, 5],
                "FixedWidthEncoding": "utf-8",
                "IncludeHeader": "True"
            }))

        with open(self.input_file, "w", encoding="utf-8") as f:
            f.write("12345ABCDEabcde\n67890FGHIJfghij\n")

    def tearDown(self):
        os.remove(self.input_file)
        os.remove(self.output_file)
        os.remove(self.spec_file)

    def test_parse_fixed_width(self):
        parse_fixed_width_to_csv(self.input_file, self.output_file, self.spec_file)
        with open(self.output_file, "r", encoding="utf-8") as f:
            lines = f.readlines()
            self.assertEqual(lines[0].strip(), "f1,f2,f3")
            self.assertEqual(lines[1].strip(), "12345,ABCDE,abcde")
            self.assertEqual(lines[2].strip(), "67890,FGHIJ,fghij")

if __name__ == "__main__":
    unittest.main()
