import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dateSelector import date_selection
from scraper import scrape_date

""" Replace the credentials section with your own Spotify developer credentials """
# grab credentials
creds = []
with open(file='creds.txt', mode="r") as file:
    for line in file:
        creds.append(line)
clientID = creds[0].split('=')[1].strip()
clientSecret = creds[1].split('=')[1].strip()
clientUsername = creds[2].split('=')[1].strip()

# authorize w/ spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=clientID,
                                               client_secret=clientSecret,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               cache_path="token.txt",
                                               username=f"{clientUsername}"))

# get user ID
userID = sp.current_user()['id']

# grab date and generate list of songs
date = date_selection()
song_list = scrape_date(date)

# create playlist
playlistName = f'Billboard Hot 100 for {date}!'
playlist = sp.user_playlist_create(user = userID, name = playlistName, public=False, description=f"The Billboard's Hot 100 songs for {date} generated with Python")
print(f"New playlist created: {playlistName}!\n")

# generate a lsit of song URIs
uriList = []
for song in song_list:
    data = sp.search(q=f"track:{song}", type="track")
    try:
        uri = data['tracks']['items'][0]['uri']
        uriList.append(uri)
        print(f"{song} found!")
    except:
        print(f"{song} is not on Spotify. Skipped.\n")
        
# add all songs to playlist
print(f"Adding songs to playlist now.\n")
sp.playlist_add_items(playlist_id = playlist['id'], items = uriList)
print(f"Finished adding all songs to playlist: {playlistName}")