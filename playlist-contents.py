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

results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=100)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=200)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=300)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=400)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=500)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=600)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=700)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=800)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=900)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=1000)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=1100)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=1200)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=1300)
print (json.dumps(results, indent=4))
results = sp.user_playlist_tracks(username, playlist_id, limit=100, offset=1400)
print (json.dumps(results, indent=4))

# for i, item in enumerate(results['tracks']):
#     print (i, item['name'])
# print