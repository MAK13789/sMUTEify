'''
MAKE EVERYTHING INTO FUNCTIONS PROBABLY, AND MAKE THE MUTING PART

ALSO UPDATE THE ACCESS TOKEN EVERY MINUTE OR SOMETHING BECAUSE IT CHANGES (TO DO THIS, MAKE EVERYTHING INTO FUNCTIONS)

WHEN PUTTING ON GITHUB, DON'T SHOW CLIENT ID, SECRET, AND ACCESS TOKEN PUBLICLY
'''
import requests
CLIENT_ID = 'yourclientid'   #hidden for privacy
CLIENT_SECRET = 'yourclientsecret'  #hidden for privacy
import spotipy.util as util
username = 'yourusername'   #hidden for privacy 
redirect_uri = 'http://localhost:7777/callback'
scope = 'user-read-currently-playing'
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
print (r)
