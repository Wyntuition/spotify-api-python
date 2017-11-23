# Spotify API with Spotipy

## Setup

### 1. Setup auth in environment variables

You can set the below environment variables for API calls. Calls that use the client credentials flow will use them and calls that use the authorization code flow will have the id passed first.

```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

### 2. Try some API calls with the included Python scripts

Install Python3 if you don't have it, and try these examples of some of the scripts.

#### Save your top tracks to a file (short, medium and long term)

```bash
python3 top-tracks-for-user.py echo ${SPOTIPY_CLIENT_ID} >> top-tracks-<DATE>.md`
```

#### Save your top artists to a file (short, medium and long term)

```bash
./save-top-artists.sh
```

#### Save x playlist

```bash
./save-playlist-tracks.sh
```
