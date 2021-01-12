# Creates a playlist for a user
import spotipy
import datetime
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

def main():
    # Setup Spotipy
    scope = "playlist-modify-public"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
    user_id = sp.me()['id']
    
    # Create new playlist
    sp.user_playlist_create(user_id, 'KEXP Import ' + datetime.date.today().strftime("%B %d, %Y"))
    
    # Parse KEXP output
    with open("KexpSavedTracks.html") as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    data = []
    table = soup.table
    rows = table.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele])
    
    tracks = [sub_list[0] for sub_list in data[1:]]
    artists = [sub_list[1] for sub_list in data[1:]]

    # Find Spotify track ID for each track, add to playlist
    track_ids = []
    errors = []
    for track, artist in zip(tracks, artists):
        potential_track_ids = sp.search(q='artist:' + artist + ' track:' + track, type='track')
        try:
            track_id = potential_track_ids['tracks']['items'][0]['id']
            track_ids.append(track_id)
        except IndexError:
            errors.append(track)

    # Write to file missing tracks
    with open("errors.txt", "w") as outfile:
        outfile.write("\n".join(errors))

    for id in track_ids:
        #can't be a string...
        test = []
        test.append(id)
        sp.playlist_add_items("25AR4X93EsmDsJS5VpqwAE", test) #hardcoded playlist

if __name__ == '__main__':
    main()