import spotipy
import spotipy.util as sp_util
from spotipy.oauth2 import SpotifyClientCredentials  
import re
import subprocess as x
import sys

print("Under contruction!!! DO NOT RUN")
sys.exit()



# #Authentication - without user
client_credentials_manager = SpotifyClientCredentials(client_id="1ba6f73518864f2e93e6fc5a643d475a", client_secret="248e285fcfdf4537a73f7bd4b1f717a3")
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

# #getting the tracks
linktoplaylist=input("enter link to playlist:")
playlist_URI = linktoplaylist.split("/")[-1].split("?")[0]
trackURIs = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
track_name = [x["track"]["name"] for x in sp.playlist_tracks(playlist_URI)["items"]]

#get list of instrumentals
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

#save list of intrumentals
with open("listofsongs.txt", 'w') as f:
    for s in listofsongs:
        f.write(str(s) + '\n')

with open("listofsongs.txt", 'r') as f:
    listofsongs = [line.rstrip('\n') for line in f]

x.call('cls',shell=True)
print("Text File Created with "+str(c)+" songs")


#authentication -- User OAuth2
scope1 = 'user-library-read'
scope2="playlist-modify-public"
scope3="playlist-modify-private"

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

token = sp_util.prompt_for_user_token(username, scope1, client_id='1ba6f73518864f2e93e6fc5a643d475a', client_secret='248e285fcfdf4537a73f7bd4b1f717a3', redirect_uri='http://localhost/')

#create playlist for user
with open("reference.txt", 'r') as r:
    reference=int(r.read())
reference+=1
with open("reference.txt", 'w') as r:
    r.write(str(reference))
sp.user_playlist_create(username, "Instrumental playlist created via spotipy api"+str(reference), public=True, collaborative=False, description='')



#Print saved songs
# if token:
#     sp = spotipy.Spotify(auth=token)
#     results = sp.current_user_saved_tracks()
#     for item in results['items']:
#         track = item['track']
#         print(track['name'] + ' - ' + track['artists'][0]['name'])
# else:
#     print("Can't get token for", username)