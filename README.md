# Spotify API with Spotipy

## Auth in Env Vars

```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

### Save your top tracks to a file (short, medium and long term)

`python3 top-tracks-for-user.py echo ${SPOTIPY_CLIENT_ID} >> top-tracks-<DATE>.md`

### Save your top artists to a file (short, medium and long term)

`./save-top-artists.sh`

### Save x playlist

`python playlist-contents.py > starred-paged.md`
