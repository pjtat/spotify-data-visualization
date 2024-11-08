from fetch_spotify_data import SpotifyApiClient
from modify_data_exports import ModifyDataExports

def main():
   modify_data_exports = ModifyDataExports()

   # Combine all spotify exports into one file
   modify_data_exports.combine_spotify_exports()

   # Convert duration to seconds and clean timestamp
   modify_data_exports.convert_duration_to_seconds()
   modify_data_exports.clean_timestamp()
   
   # Remove unneeded fields and rename fields
   modify_data_exports.remove_unneeded_data()
   modify_data_exports.rename_fields()

   # Remove ignored tracks, albums, and artists
   modify_data_exports.remove_ignored_items()

if __name__ == "__main__":
    main()