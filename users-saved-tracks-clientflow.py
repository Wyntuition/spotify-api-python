import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

playlists = sp.user_saved_tracks('spotify')
while tracks:
    for i, track in enumerate(tracks['items']):
        print("%4d %s %s" % (i + 1 + tracks['offset'], track['artists'][0]['name'],  track['name']))
    if tracks['next']:
        tracks = sp.next(playlists)
    else:
        tracks = None