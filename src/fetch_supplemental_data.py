import json
from fetch_spotify_data import SpotifyApiClient

def main():
   # Initialize Spotify API client
   spotify_api_client = SpotifyApiClient()

   # Initialize artist and album data
   artist_data = [
      {
            'id': '',
            'artwork_url': '',
            'genres': [],
            'albums': []
      }
   ]
   
   album_data = [
      {
            'id': '',
            'artwork_url': '',
            'release_date': ''
      }
   ]
   
   # TEMPORARY - Use test file to limit calls
   with open('test-combined_spotify_data_modified.json', 'r') as f:
      modified_data = json.load(f)

   # Pull in the existing combined export
   # with open('combined_spotify_data_modified.json', 'r') as f:
   #    modified_data = json.load(f)
   
   for item in modified_data:
      # Identify track ID and pull track information
      track_id = item['id']
      track_info = spotify_api_client.get_track_chart_info(track_id)
      
      # Identify artist ID 
      artist_id = track_info.json()['artists'][0]['id']

      # Check if the artist is already in the artist data
      if not any(artist['id'] == artist_id for artist in artist_data):
         # Pull the artist information
         artist_info = spotify_api_client.get_artist_chart_info(artist_id)

         # Add the artist information to the artist data
         artist_data.append({
               'id': artist_id,
               'artwork_url': artist_info['artist_artwork_url'],
               'genres': artist_info['genres'],
               'albums': []
         })
      
      # Identify album ID
      album_id = track_info.json()['album']['id']

      # Check if the album is already in the album data
      if not any(album['id'] == album_id for album in album_data):    
        # Pull the album information
        album_info = spotify_api_client.get_album_chart_info(album_id)

        # Add the album information to the album data
        album_data.append({
            'id': album_id,
            'artwork_url': album_info['album_artwork_url'],
            'release_date': album_info['album_release_date']
        })

      supplemental_data = {
         'artists': artist_data,
         'albums': album_data
      }

      # Overwrite the existing file with the new data
      with open('supplemental_track_data.json', 'w') as f:
         json.dump(supplemental_data, f, indent=2)

if __name__ == "__main__":
    main()