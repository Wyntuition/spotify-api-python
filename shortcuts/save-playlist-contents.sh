DATE=`date +%Y-%m-%d`

# playlist-contents.py 
# USAGE:
#   playlist-contents.py <uri of playlist> > <filename of output>

# Shortcut: 

# My Starred playlist
SPOTIFY_URI="spotify:user:127855684:playlist:2DePm7Z6OZGOwvt4BUUCTt"

python3 playlist-contents.py $SPOTIFY_URI > starred-$DATE.json