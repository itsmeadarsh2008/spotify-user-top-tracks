import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

client_id = os.environ.get("SPOTIPY_CLIENT_ID")
client_secret = os.environ.get("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.environ.get("SPOTIPY_REDIRECT_URI")
scope = os.environ.get("SPOTIPY_SCOPE")

# Initialize Spotify API client
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))

def clear_playlist(playlist_id):
    # Get the current tracks in the playlist
    current_tracks = sp.playlist_tracks(playlist_id)

    # Remove all tracks from the playlist
    track_uris = [track['track']['uri'] for track in current_tracks['items']]
    sp.playlist_remove_all_occurrences_of_items(playlist_id, track_uris)

if __name__ == '__main__':
    playlist_id_ = os.environ.get('PLAYLIST_ID')
    clear_playlist(playlist_id_)
    # Get the user's top tracks
    top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')

    # Extract track URIs and add them to the existing playlist
    track_uris = [track['uri'] for track in top_tracks['items']]
    sp.playlist_add_items(playlist_id_, track_uris)
