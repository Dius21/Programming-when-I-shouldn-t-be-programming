import spotipy
from spotipy.oauth2 import SpotifyClientCredentials  
import re
import csv
import AppOpener
import subprocess as x

#Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id="1ba6f73518864f2e93e6fc5a643d475a", client_secret="248e285fcfdf4537a73f7bd4b1f717a3")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

#getting the tracks
linktoplaylist=input("enter link to playlist:")
playlist_URI = linktoplaylist.split("/")[-1].split("?")[0]
# playlist_URI = "https://open.spotify.com/playlist/37i9dQZF1DXcBWIGoYBM5M"
trackURIs = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
track_name = [x["track"]["name"] for x in sp.playlist_tracks(playlist_URI)["items"]]
open("listofsongs", mode="w+")
listofsongs=[]
c=0
for i in range(len(track_name)):
    results = sp.search(q=f'track:{track_name[i]} instrumental', type='track')
    tracks = results['tracks']['items']
    if tracks != []:
        track_uri_indices=re.search(r"spotify:track:(.*)",tracks[0]['uri'])
        found_track_uri=track_uri_indices.group(1)
        listofsongs.append("https://open.spotify.com/track/"+found_track_uri)
        x.call('cls',shell=True)
        c+=1
        if c==0:
            print("Searching -")
        if (c%4)==1:
            print("Searching \\")
        if (c%4)==2:
            print("Searching |")
        if (c%4)==3:
            print("Searching /")
        if (c%4)==0:
            print("Searching -")

x.call('cls',shell=True)
print("Done")

with open("listofsongs.txt", 'w') as f:
    for s in listofsongs:
        f.write(str(s) + '\n')

with open("listofsongs.txt", 'r') as f:
    listofsongs = [line.rstrip('\n') for line in f]

x.call('cls',shell=True)
print("Text File Created with "+str(c)+" songs")

# AppOpener.open("Power automate")