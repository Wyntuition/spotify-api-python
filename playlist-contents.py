from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import json

client_credentials_manager = SpotifyClientCredentials()
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = 'spotify:user:127855684:playlist:2DePm7Z6OZGOwvt4BUUCTt'
username = uri.split(':')[2]
playlist_id = uri.split(':')[4]

results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=0)
print (json.dumps(results, indent=4))

for x in range(0, 20):
  results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=(x * 100))
  print (json.dumps(results, indent=4))

# Spotify will only return 100 at a time, so this is a temp hack to get a larger playlist.


# for i, item in enumerate(results['tracks']):
#     print (i, item['name'])
# print