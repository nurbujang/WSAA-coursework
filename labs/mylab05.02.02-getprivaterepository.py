import requests
import json
from mylab5config import config as cfg

filename = "mylab5repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://api.github.com/repos/nurbujang/private'

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey}
#response = requests.get(url, headers= headers)

apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey))

print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)

























# ok this is not exactly like I asked you to to in the labs
# import requests
# import json
# from config import config as cfg

# filename = "repos-private.json"

# #url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
# url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'

# # the more basic way of setting authorization
# #headers = {'Authorization': 'token ' + apikey}
# #response = requests.get(url, headers= headers)

# apikey = cfg["githubkey"]
# response = requests.get(url, auth = ('token', apikey))

# print (response.status_code)
# #print (response.json())

# with  open(filename, 'w') as fp:
#     repoJSON = response.json()
#     json.dump(repoJSON, fp, indent=4)