import json
import os
import logging

from fetch_spotify_data import SpotifyApiClient

def main():
   # Set up logging configuration
   logging.basicConfig(
       filename='data/logs/fetch_supplemental.log',
       level=logging.INFO,
       format='%(asctime)s - %(message)s',
       datefmt='%Y-%m-%d %H:%M:%S'
   )
   
   # Initialize Spotify API client
   spotify_api_client = SpotifyApiClient()
   
   # TEMPORARY - Use test file to limit calls
   # UPDATE to use real file when ready
   test_file_path = 'data/test/test-combined_spotify_data_modified.json'
   with open(test_file_path, 'r') as f:
       modified_data = json.load(f)

   # Pull in existing supplemental data list
   if os.path.exists('data/processed/supplemental_track_data.json'):
      with open('data/processed/supplemental_track_data.json', 'r') as f:
         supplemental_data = json.load(f)
      supplemental_artist_data = supplemental_data['artists']
      supplemental_album_data = supplemental_data['albums']
   else:
      with open('data/processed/supplemental_track_data.json', 'w') as f:
         json.dump({}, f, indent=2)
      supplemental_artist_data = []
      supplemental_album_data = []
         
   for item in modified_data:
      # Identify track ID and pull track information
      track_id = item['id']
      track_info = spotify_api_client.get_track_chart_info(track_id)
      
      # Identify artist ID and album ID
      artist_id = track_info['album']['artists'][0]['id']
      album_id = track_info['album']['id']

      # Check if artist exists in current data
      artist_exists = any(artist['artist_id'] == artist_id for artist in supplemental_artist_data)
      logging.info(f"Checking artist {artist_id}: {'exists' if artist_exists else 'new'}")
      
      # If the artist is not in the supplemental data, pull the artist information
      if not artist_exists:
         # Pull the artist information
         artist_info = spotify_api_client.get_artist_chart_info(artist_id)
         
         # Add the artist information to the artist data
         supplemental_artist_data.append({
               'artist_id': artist_id,
               'artwork_url': artist_info['images'][0]['url'],
               'genres': artist_info['genres']
         })

      album_exists = any(album['album_id'] == album_id for album in supplemental_album_data)
      logging.info(f"Checking album {album_id}: {'exists' if album_exists else 'new'}")

      # If the album is not in the supplemental data, pull the album information
      if not album_exists:
         # Pull the album information
         album_info = spotify_api_client.get_album_chart_info(album_id)

         # Add the album information to the album data
         supplemental_album_data.append({
               'album_id': album_id,
               'artwork_url': album_info['images'][0]['url'],
               'release_date': album_info['release_date']
        })

      supplemental_data = {
         'artists': supplemental_artist_data,
         'albums': supplemental_album_data
      }

      # Overwrite the existing file with the new data
      with open('data/processed/supplemental_track_data.json', 'w') as f:
         json.dump(supplemental_data, f, indent=2)

if __name__ == "__main__":
   main()