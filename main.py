"""
1. Read csv files
2. Important columns: Series Number, Filename, Description, UUID
3. Create a dictionary of CHIP-0007 format
4. Write Json to output file
5. Convert Json string to HASH
"""

import csv
import hashlib
import json
import os


CHIPS_DIR = "chips"


def create_chips(filename: str, team_name: str):
    """Create CHIP-0007 format json rows for a given csv file

    :param filename: filename of the csv file
    :type filename: str
    :param team_name: team name that is minting the chips
    :type team_name: str
    """

    # Create an output directory for the team if none exists
    if not os.path.exists(team_name):
        os.makedirs(team_name)

    # Read csv file
    with open(filename, 'r') as csvfile:

        # Create a dictionary reader, skip the first row
        reader = csv.DictReader(csvfile)

        # Get file name without extension: "chips.csv" -> "chips"
        main_filename = filename.split('.')[0]

        # Create the output CSV file name: <filename>_output.csv
        output_filename = main_filename + ".output.csv"

        # Change directory to team name
        # So that all the output files for a team are in the same directory
        # It makes everything easier and cleaner
        os.chdir(team_name)

        # Create a new csv file to write the output
        with open(output_filename, 'w') as output_file:
            # Write the header row first
            fieldnames = reader.fieldnames
            output_file.write(','.join(fieldnames) + '\n')

            # Create CHIPS_DIR directory if none exists
            if not os.path.exists(CHIPS_DIR):
                os.makedirs(CHIPS_DIR)

            # Loop through each row of csv file, create CHIP-0007 format
            # dictionary, get the hash of the json string and write it to the
            # output csv file
            for row in reader:
                chip_dict = create_chip_0007_dict(team_name, row)
                hash_str = write_json_get_hash(chip_dict)
                row['Hash'] = hash_str

                # Write to output file without new line
                output_file.write(','.join(row.values()) + '\n')


def create_new_chip_template():
    """Create a new chip template dictionary"""
    return {
        "format": "CHIP-0007",
        "name": "",
        "description": "",
        "minting_tool": "",
        "sensitive_content": False,
        "series_number": 0,
        "series_total": 400,
        "attributes": [],
        "collection": {
            "name": "Zuri NFT Tickets for Free Lunch",
            "id": "",
            "attributes": []
        },
        "data": {}
    }


def create_chip_0007_dict(team_name: str, row: dict):
    """Create a dictionary of CHIP-0007 format
    for a given row of csv file"""
    chip_0007_dict = create_new_chip_template()

    chip_0007_dict["name"] = row['Filename']
    chip_0007_dict["series_number"] = row['Series Number']
    chip_0007_dict["minting_tool"] = team_name
    chip_0007_dict["description"] = row['Description']
    chip_0007_dict["collection"]["id"] = row['UUID']

    return chip_0007_dict


def write_json_get_hash(data: dict) -> str:
    """
    Write Json to output file, convert Json string to HASH, return HASH
    """

    filename = os.path.join(CHIPS_DIR, data["name"] + "output.json")

    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)

    with open(filename, 'r') as outfile:
        json_string = outfile.read()

    return hashlib.sha256(json_string.encode()).hexdigest()


# Create CLI for the script
if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Create CHIP-0007 Json file')
    parser.add_argument('-f', '--file', help='CSV file to read', required=True)
    parser.add_argument('-t', '--team', help='Team Name', required=True)
    args = parser.parse_args()

    create_chips(args.file, args.team)
