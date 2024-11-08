import requests 
from config import CLIENT_ID, CLIENT_SECRET 

class SpotifyApiClient: 
    def __init__(self):
        self.access_token = self._get_access_token()

    def _get_access_token(self):
        # Define the endpoint and your credentials
        url = "https://accounts.spotify.com/api/token"
        client_id = CLIENT_ID
        client_secret = CLIENT_SECRET

        # Get access token
        auth_response = requests.post(url, {
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret,
        })

        # Convert response to JSON
        auth_response_data = auth_response.json()

        return auth_response_data['access_token']
    
    def get_artist_genres(self, artist_id):
        # Get artist genres from Spotify API
        url = f"https://api.spotify.com/v1/artists/{artist_id}"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            raise Exception(f"Error getting genres: {response.status_code}")
        
        # Extract genres from response
        genres = response.json().get('genres', [])
        
        return genres

    def get_artist_artwork(self, artist_id):
        # Get artist artwork Spotify API
        url = f"https://api.spotify.com/v1/artists/{artist_id}"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        
        response = requests.get(url, headers=headers)
        
        # Check if request was successful
        if response.status_code != 200:
            raise Exception(f"Error getting genres: {response.status_code}")
        
        # Get the first image URL if available, otherwise return None
        artist_artwork = response.json().get('images', [])[0]['url']
        
        return artist_artwork
        
    def get_album_artwork(self, album_id):
        # Get album artwork Spotify API
        url = f"https://api.spotify.com/v1/tracks/{album_id}"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        
        response = requests.get(url, headers=headers)
        
        # Check if request was successful
        if response.status_code != 200:
            raise Exception(f"Error getting genres: {response.status_code}")
        
        album_artwork = response.json().get('images', [{}])[0].get('url', None)
        
        return album_artwork
    
    def get_track_release_date(self, track_id):
        # Get release date from Spotify API
        url = f"https://api.spotify.com/v1/tracks/{track_id}"  

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            raise Exception(f"Error getting release date: {response.status_code}")
        
        # Release date is nested in the album object
        release_date = response.json().get('album', {}).get('release_date', None)
        
        return release_date