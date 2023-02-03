import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_credentials_manager = SpotifyOAuth(client_id="1ba6f73518864f2e93e6fc5a643d475a", client_secret="248e285fcfdf4537a73f7bd4b1f717a3")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_url = input("Enter the URL of the playlist: ")
playlist_id = playlist_url.split("/")[-1]
result = sp.playlist(playlist_id)
tracks = result["tracks"]["items"]

# Create a list of all the songs in the playlist
song_list = []
for track in tracks:
    song_list.append(track["name"])

# Search for instrumental versions of each song in the song_list
instrumental_list = []
for song in song_list:
    query = song + " instrumental"
    result = sp.search(q=query, type="track")
    tracks = result["tracks"]["items"]
    if len(tracks) > 0:
        instrumental_list.append(tracks[0]["name"])
    else:
        print(f"No instrumental version found for {song}")

# Print the list of instrumental versions
print("Instrumental versions:")
for instrumental in instrumental_list:
    print(instrumental)
