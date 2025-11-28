#!/usr/bin/python3
"""Convert CSV data to JSON format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """salam"""
    try:
        # Read CSV file
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data_list = [row for row in reader]

        # Serialize
        with open('data.json', 'w') as jsonfile:
            json.dump(data_list, jsonfile, indent=4)

        return True

    except FileNotFoundError:
        # File not found
        return False
    except Exception:
        # Any error
        return False
