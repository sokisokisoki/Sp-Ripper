
import spotipy
import webbrowser
import re

from spotipy.oauth2 import SpotifyClientCredentials

from PlaylistObj import PlaylistObj

def extract_user(string):
    index = string.find("user/")  # Find the index of "user/"
    if index != -1:  # If "user/" is found
        return string[index + len("user/"):]  # Extract everything after "user/"
    else:
        return None  # Return None if "user/" is not found




def extract_user_id(url):
    match = re.search(r"user/(.*?)(\?|$)", url)
    if match:
        return match.group(1)
    return None

#taken from https://stackoverflow.com/a/39113522    
def get_playlist_tracks(username,playlist_id):
    results = sp.user_playlist_tracks(username,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks



auth_manager = SpotifyClientCredentials()
#sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
sp = spotipy.Spotify(auth_manager=auth_manager)


userLink = str(input('\nPlease type in your spotify account url i.e.(https://open.spotify.com/user/your_name): '))
print("\n")


#fields are display_name, external_urls(spotify), href, id, images, type, uri, followers
userID = extract_user_id(userLink)
username = sp.user(userID)

display_name = username['display_name']

#playlists_names = []

playlists_info = sp.user_playlists(userID)
playlists_names = playlists_info['items']

while playlists_info['next']:
    playlists_info = sp.next(playlists_info)
    playlists_names.extend(playlists_info['items'])

k = True
pl_cnt = 1
pl_numPairs= {}


if len(playlists_names) == 0:
    print("Unable to find any playlists for given account, make sure that your account link is correct and your playlists and account are set to public")
    k = False

else:
    for pl in playlists_names:
        print('{}\t {}'.format(pl_cnt, pl['name']))
        pl_numPairs[str(pl_cnt)] = pl
        pl_cnt += 1


print("\n")


usedPL = []
focus = input("Please input a number from the list to select a playlist, or type \"all\" ")
print("\n")

usedPL.append(focus)

#initial loop to collect what needs to be parsed
while k:
    
    if(focus == "all"):
        #loop and make dict
        k = False
        break

    elif(focus == 'quit'):
            break

    elif(focus.isnumeric()): #checks if passed in value is: an int, within range of list
        if(int(focus) > 0 and int(focus) <= len(playlists_names)):
            usedPL.append(focus)
            print('\n')

            currPL = pl_numPairs[focus]
            print(currPL['name'])
            print()

            #tracks = get_playlist_tracks(userID, playlists_info[focus])

        else:
            print('Invalid input\n')

    else:
        print('Incorrect input please try again\n')

    cont = input("Do you want to input another playlist? (y/n) ")

    if (cont == 'n'):
        break

    print("\n")
    t = True
    while t:
        focus = input("Please input a number from the list to select a playlist, or type \"all\" ")
        if focus in usedPL:
            print('Incorrect input please try again\n')

            cont = input("Do you want to input another playlist? (y/n) ")

            if (cont == 'n'):
                break

        else:
            t = False

    if (cont == 'n'):
        break

    print("")

#limited dict of playlists in use
activePLs = {}

if focus == 'all':
    activePLs = pl_numPairs

else:
    for num in usedPL:
        activePLs[num] = pl_numPairs[num]


#list of playlist objs
plObjs = []

for items in activePLs:
    currPL = activePLs[items]

    tracklist = sp.playlist_tracks(currPL['id'])
    tracks = tracklist['items']
    while tracklist['next']:
        tracklist = sp.next(tracklist)
        tracks.extend(tracklist['items'])

    #isolated song list
    tL = []

    for track in tracks:
        
        trackName = track['track']

        try:
            songDesc = trackName['name'] + ' by '

            if len(trackName['artists']) == 1:
                songDesc += trackName['artists'][0]['name']

            else:
                aList = []
                for arts in trackName['artists']:
                    aList.append(arts['name'])

                songDesc += f"{', '.join(aList)}"

            tL.append(songDesc)

        except:
            print('No song name found. Skipped')
            print(track)

    

    plObj = PlaylistObj(currPL['name'])
    plObj.addTracks(tL)
    plObj.setURL(currPL['images'][0]['url'])


    plObjs.append(plObj)