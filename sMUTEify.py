import requests
import spotipy.util as util
import pyautogui
import time
CLIENT_ID = 'yourclientid'   #can be obtained from spotify's developer website
CLIENT_SECRET = 'yourclientsecret'   #can also be obtained from spotify's developer website
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
def mute():
    pyautogui.press('volumemute')   
def unmute(x):
    if x % 2 == 0:
        pyautogui.press('volumedown')
    else:
        pyautogui.press('volumeup')
count = 0
while True:
    if is_song_playing() == False:
        mute()
        time.sleep(30)
        unmute(count)
        count += 1
    time.sleep(1)
