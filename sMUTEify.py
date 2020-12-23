'''
FIGURE OUT HOW TO GET THE ACCESS TOKEN AUTOMATICALLY
'''
import requests
CLIENT_ID = 'yourclientid'   #hiding for privacy
CLIENT_SECRET = 'yourclientsecret'   #hiding for privacy


'''
AUTH_URL = 'https://accounts.spotify.com/api/token'
auth_response = requests.post(AUTH_URL, {
    'grant_type': 'client_credentials',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})
auth_response_data = auth_response.json()
access_token = auth_response_data['access_token']
'''

#access_token taken manually from the website (https://developer.spotify.com/console/get-users-currently-playing-track/?market=&additional_types=):
access_token = 'youraccesstoken'   #hiding for privacy


headers = {
    'Authorization': 'Bearer {token}'.format(token=access_token)
}



#getting info for a song (just using this as an example to test this stuff):
'''
BASE_URL = 'https://api.spotify.com/v1/'
track_id = '7lQWRAjyhTpCWFC0jmclT4'
r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)
r = r.json()
print (r)
'''


r = requests.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
r = r.json()
print (r)
