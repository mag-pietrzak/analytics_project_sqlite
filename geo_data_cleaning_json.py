import logging
import json

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Input and output filenames
original_data = 'geonames-postal-code@public.json'
output_data = 'formatted_zipcodes.json'

# Load the JSON data from the input file
with open(original_data, 'r') as file:
    data = json.load(file)

# Formatting the JSON data with indentation
formatted_json = json.dumps(data, indent=4)

# Save the formatted JSON to the output file
with open(output_data, 'w') as file:
    file.write(formatted_json)

logging.info(f"Formatted JSON has been saved to '{output_data}'.")