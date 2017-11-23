# Spotify API with Spotipy

Quickly interact with the Spotfiy API, using a Python wrapper called [Spotipy](https://github.com/plamere/spotipy). This sample includes backing up a playlist, and getting your own top artists & tracks over the short, mid and long term.

## Setup

### 1. Setup auth in environment variables

If you don't have one, you can get a client id and secret key from Spotify through their [registration process](https://developer.spotify.com/my-applications/) for access to the API calls.

Set your environment variables with the values. One way would be to put them in a .env file and run `source .env`:

```bash
export SPOTIPY_CLIENT_ID='your-spotify-client-id'
export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
export SPOTIPY_REDIRECT_URI='your-app-redirect-url'
```

### 2. Try some API calls with the included Python scripts

Install Python3 if you don't have it, as well as these libraries, `pip install spotipy simplejson`, and try these examples of some of the scripts:

#### Save your top tracks to a file (short, medium and long term)

This calls the Python script, passing the Spotify client ID, and piping the text to the specified file. Once you see what's happening, you can call the shortcut script which does the same thing, `shortcuts/save-top-tracks.sh`.

```bash
python3 top-tracks-for-user.py echo ${SPOTIPY_CLIENT_ID} >> top-tracks.md
```

#### Save your top artists to a file (short, medium and long term) shortcut

```bash
./shortcuts/save-top-artists.sh
```

#### Save x playlist shortcut

```bash
./shortcuts/save-playlist-tracks.sh
```

#### Authorization code flow vs client credentials flow

To access personal data, you should use authorization code flow (used in most of the scripts unless labels 'clientflow'), as client credentials flow doesn't support authorization but has a higher rate limit.