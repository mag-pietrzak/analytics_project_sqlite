import logging
import json
import os
from main.config import clean_path

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def geo_data_formatting():
    # Input and output filenames
    original_data = 'data_generate/json_files/formatted_zipcodes.json'
    output_data = 'formatted_and_cleaned_zipcodes.json'

    # Open and load the JSON file
    with open(original_data, "r") as json_file:
        data = json.load(json_file)

    # Check if the data is a list
    if isinstance(data, list):
        formatted_and_cleaned_zipcodes = []
        for entry in data:
            # Extract only the needed fields from each entry
            formatted_entry = {
                "postal_code": entry.get("postal_code"),
                "admin_name1": entry.get("admin_name1"),
                "admin_code1": entry.get("admin_code1"),
                "latitude": entry.get("latitude"),
                "longitude": entry.get("longitude")
            }
            formatted_and_cleaned_zipcodes.append(formatted_entry)
    else:
        # Handle the case if the data is not a list
        logging.info("Expected a list of entries in the JSON file.")
        return
    
    file_path_geo = os.path.join(clean_path, "formatted_and_cleaned_zipcodes.json")

    with open(file_path_geo, "w") as output_file:
        json.dump(formatted_and_cleaned_zipcodes, output_file, indent=4)

    logging.info(f"Data has been formatted and saved to {output_data}")

if __name__ == "__main__":
    geo_data_formatting()