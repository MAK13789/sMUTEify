'''
FIGURE OUT HOW TO GET THE ACCESS TOKEN AUTOMATICALLY
'''
import requests
CLIENT_ID = 'a455f73c6eac46428cb7f35d75e842f8'
CLIENT_SECRET = '9bf9b5fce0b147dca5adb1758711e85d'


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
access_token = 'BQCEdkJzrEkS-pNXRy6H1NAxF27aSCW5vaA3H2Zj4xMdIjLYPkykSs35_-t7ayvQJMD39WeXOJnzqZ-33iCjS_lXBfa74KWYuVx3hjdNfOLg2ka2VnqRG3WWPvqEpWv9hL99a6KW9qitBjvyta71KASG2P2f3h1oxDqp'


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