import os
from os.path import dirname
import json
from config import IGNORE_ARTISTS, IGNORE_ALBUMS, IGNORE_TRACKS

class ModifyDataExports:
    def __init__(self):
        self.export_path = os.path.join(dirname(dirname(__file__)), 'exported_data')

    def combine_spotify_exports(self):
        # Initialize an empty list to hold all JSON data
        combined_spotify_export = []

        # Loop through each file in the specified directory
        for filename in os.listdir(self.export_path):
            if filename.endswith('.json'):
                file_path = os.path.join(self.export_path, filename)
                with open(file_path, 'r') as f:
                    # Load the JSON data from the file
                    data = json.load(f)
                    # Ensure the data is a list and extend the combined_data list
                    if isinstance(data, list):
                        combined_spotify_export.extend(data)

        # Write the combined data to a new JSON file
        output_file_raw = 'combined_spotify_data_raw.json'
        output_file_modified = 'combined_spotify_data_modified.json'

        with open(output_file_raw, 'w') as f:
            json.dump(combined_spotify_export, f, indent=2)
        
        with open(output_file_modified, 'w') as f:
            json.dump(combined_spotify_export, f, indent=2)

    
    def remove_unneeded_data(self):
        # Pull in the existing combined export
        with open('combined_spotify_data_modified.json', 'r') as f:
            modify_data = json.load(f)
            
        # List of fields to remove
        fields_to_remove = [
            'username',
            'platform',
            'ip_addr_decrypted',
            'user_agent_decrypted',
            'episode_name',
            'episode_show_name',
            'spotify_episode_uri',
            'offline',
            'offline_timestamp',
            'incognito_mode'
        ]
        
        # Remove unneeded fields 
        for item in modify_data:
            for field in fields_to_remove:
                if field in item:
                    del item[field]
        
        # Overwrite the existing file with the new data
        with open('combined_spotify_data_modified.json', 'w') as f:
            json.dump(modify_data, f, indent=2)

    def convert_duration_to_seconds(self):
        # Pull in the existing combined export
        with open('combined_spotify_data_modified.json', 'r') as f:
            modify_data = json.load(f)

        # Convert duration to seconds
        for item in modify_data:
            item['ms_played'] = round(item['ms_played'] / 1000, 2)

        # Overwrite the existing file with the new data
        with open('combined_spotify_data_modified.json', 'w') as f:
            json.dump(modify_data, f, indent=2)

    def clean_timestamp(self):
        # Pull in the existing combined export
        with open('combined_spotify_data_modified.json', 'r') as f:
            modify_data = json.load(f)

        # Clean up the timestamp
        for item in modify_data:
            # Remove the 'Z' and replace 'T' with a space
            item['Timestamp'] = item['Timestamp'].replace('Z', '').replace('T', ' ')

        # Overwrite the existing file with the new data
        with open('combined_spotify_data_modified.json', 'w') as f:
            json.dump(modify_data, f, indent=2)

    def rename_fields(self):
        # Pull in the existing combined export
        with open('combined_spotify_data_modified.json', 'r') as f:
            modify_data = json.load(f)

        fields_to_rename = {
            'ts': 'Timestamp',
            'ms_played': 'Play Duration (s)',
            'conn_country': 'Country Listened',
            'master_metadata_track_name': 'Track',
            'master_metadata_album_artist_name': 'Arist',
            'master_metadata_album_album_name': 'Album',
            'spotify_track_uri': 'Track URL',
            'reason_start': 'Start Reason',
            'reason_end': 'End Reason',
            'shuffle': 'Shuffle',
            'skipped': 'Skipped'
        }

        #  Rename the fields
        for item in modify_data:
            for old_name, new_name in fields_to_rename.items():
                if old_name in item:
                    item[new_name] = item.pop(old_name)

        # Overwrite the existing file with the new data
        with open('combined_spotify_data_modified.json', 'w') as f:
            json.dump(modify_data, f, indent=2)
    
    def remove_ignored_items(self):
        # Pull in the existing combined export
        with open('combined_spotify_data_modified.json', 'r') as f:
            modify_data = json.load(f)

        # Remove ignored items
        for item in modify_data:
            if item['Arist'] in IGNORE_ARTISTS:
                modify_data.remove(item)
            if item['Album'] in IGNORE_ALBUMS:
                modify_data.remove(item)
            if item['Track'] in IGNORE_TRACKS:
                modify_data.remove(item)    

        # Overwrite the existing file with the new data
        with open('combined_spotify_data_modified.json', 'w') as f:
            json.dump(modify_data, f, indent=2) 