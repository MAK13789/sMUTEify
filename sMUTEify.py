'''
MAKE THE MUTING PART

ALSO UPDATE THE ACCESS TOKEN EVERY MINUTE OR SOMETHING BECAUSE IT CHANGES (TO DO THIS, MAKE EVERYTHING INTO FUNCTIONS)
'''
import requests
import spotipy.util as util
CLIENT_ID = 'yourclientid'
CLIENT_SECRET = 'yourclientsecret'
username = 'yourusername' 
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-currently-playing'
def is_song_playing():
    global CLIENT_ID, CLIENT_SECRET, username, redirect_uri, scope
    access_token = util.prompt_for_user_token(username=username, 
                                   scope=scope, 
                                   client_id=CLIENT_ID,   
                                   client_secret=CLIENT_SECRET,     
                                   redirect_uri=redirect_uri)
    headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
    }
    r = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
    r = r.json()
    if r['currently_playing_type'] == 'ad':
        return False
    return True
print (is_song_playing())
