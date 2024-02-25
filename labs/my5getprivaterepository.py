import requests
import json
#from config import config as cfg

#GET INFO FROM Private REPO: >

# filename = "my5repos-private.json"

# url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'

# response = requests.get(url) # no authorisation here yet
# print (response.status_code)

# with  open(filename, 'w') as fp:
#     repoJSON = response.json()
#     json.dump(repoJSON, fp, indent=4)

# run that, will get error 404 not found bc u dont have autorization, so as if it doesnt exist

# so get a key from owner andrewbeattycourseware profile > settings > developer settings > personal access token
# > fine grained token > generate new token > select repo, expire asap, permissions only to content

#--------------------------------------------------------------------------------------------------
    
filename = "my5repos-private.json"

#url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
url = 'https://api.github.com/repos/nurbujang/private'

# this token is no longer valid, becuase it has been pushed to GitHub
# GitHub detects it and invalidates it automatically for security
apikey='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' # finegrained token from owner

# the more basic way of setting authorization
#headers = {'Authorization': 'token ' + apikey} # old way
#response = requests.get(url, headers= headers) # old way

#apikey = cfg["githubkey"]
response = requests.get(url, auth = ('token', apikey)) # new way
print (response.status_code)
#print (response.json())

with  open(filename, 'w') as fp:
    repoJSON = response.json()
    json.dump(repoJSON, fp, indent=4)










# filename = "repos-private.json"

# #url = 'https://api.github.com/repos/andrewbeattycourseware/datarepresentation/contents/code'
# url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'

# # this token is no longer valid, becuase it has been pushed to GitHub
# # GitHub detects it and invalidates it automatically for security
# apikey='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'
# # the more basic way of setting authorization
# #headers = {'Authorization': 'token ' + apikey}
# #response = requests.get(url, headers= headers)

# #apikey = cfg["githubkey"]
# response = requests.get(url, auth = ('token', apikey))

# print (response.status_code)
# #print (response.json())

# with  open(filename, 'w') as fp:
#     repoJSON = response.json()
#     json.dump(repoJSON, fp, indent=4)
