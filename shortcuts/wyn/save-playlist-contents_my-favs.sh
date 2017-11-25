DATE=`date +%Y-%m-%d`

# My Absolute Favorites playlist
SPOTIFY_URI="spotify:user:127855684:playlist:59kzNR07zZwO0SPjJB8mlw"
OUTPUT_FILENAME="abs-favorites"

python3 playlist-contents.py $SPOTIFY_URI > $OUTPUT_FILENAME-$DATE.json

# Starred playlist
SPOTIFY_URI="spotify:user:127855684:playlist:2DePm7Z6OZGOwvt4BUUCTt"
OUTPUT_FILENAME="starred"

python3 playlist-contents.py $SPOTIFY_URI > $OUTPUT_FILENAME-$DATE.json