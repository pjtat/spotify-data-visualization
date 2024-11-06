import os
import json

dirname = os.path.dirname
export_path = os.path.join(dirname(dirname(__file__)), 'exported_data')

# Initialize an empty list to hold all JSON data
combined_spotify_export = []

# Loop through each file in the specified directory
for filename in os.listdir(export_path):
    if filename.endswith('.json'):
        file_path = os.path.join(export_path, filename)
        with open(file_path, 'r') as f:
            # Load the JSON data from the file
            data = json.load(f)
            # Ensure the data is a list and extend the combined_data list
            if isinstance(data, list):
                combined_spotify_export.extend(data)

# Specify the output file
output_file = 'combined_spotify_data.json'

# Write the combined data to a new JSON file
with open(output_file, 'w') as f:
    json.dump(combined_spotify_export, f, indent=2)

print(f"Combined JSON data written to {output_file}")
