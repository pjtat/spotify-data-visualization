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

    def get_artist_chart_info(self, artist_id):
        # Get artist genres from Spotify API
        url = f"https://api.spotify.com/v1/artists/{artist_id}"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(url, headers=headers)

        # Check if request was successful
        if response.status_code != 200:
            error_body = response.json() if response.content else "No error details"
            print(f"Failed request for artist: {artist_id}")
            print(f"Response body: {error_body}")
            raise Exception(f"Error getting artist info: {response.status_code}")
        
        return response.json()
        
    def get_album_chart_info(self, album_id):
        # Get album artwork Spotify API
        url = f"https://api.spotify.com/v1/albums/{album_id}"

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }
        
        response = requests.get(url, headers=headers)
        
        # Check if request was successful
        if response.status_code != 200:
            error_body = response.json() if response.content else "No error details"
            print(f"Failed request for album: {album_id}")
            print(f"Response body: {error_body}")
            raise Exception(f"Error getting album info: {response.status_code}")
        
        return response.json()
    
    def get_track_chart_info(self, track_id):
        # Get release date from Spotify API
        url = f"https://api.spotify.com/v1/tracks/{track_id}"  

        headers = {
            "Authorization": f"Bearer {self.access_token}"
        }

        response = requests.get(url, headers=headers)

        # Add debugging information
        print(f"Status Code: {response.status_code}")
        print(f"Response Content: {response.content}")
        
        if response.status_code != 200:
            print(f"Error response headers: {response.headers}")
            return None
        
        try:
            return response.json()
        except requests.exceptions.JSONDecodeError as e:
            print(f"Failed to decode JSON: {e}")
            print(f"Raw response: {response.text}")
            return None