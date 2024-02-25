import requests
import json

# https://docs.github.com > Rest API > Repositories > Repositories > List repositories  for a user 
# > cURL > get the https..> copy into my5getrepoinformation.py

# GET INFO FROM PUBLIC REPO:

# filename = "my5repos-public.json"

# url = 'https://api.github.com/users/USERNAME/repos'

# response = requests.get(url)
# print (response.status_code)
# repoJSON = response.json()
# #print (response.json())

# with  open(filename, 'w') as fp:
#     json.dump(repoJSON, fp, indent=4)

# change USERNAME to your name

#================================================================

# filename = "my5repos-public.json"

# url = 'https://api.github.com/users/nurbujang/repos'

# response = requests.get(url)
# print (response.status_code) # make sure u get 200
# repoJSON = response.json() # turn into json
# #print (response.json())

# with  open(filename, 'w') as fp: # save into file called my5repos-public.json
#     json.dump(repoJSON, fp, indent=4)

# run this, check my5repos-public.py
    # if >30 repositories, default is 30, so use pagination in the REST API

#------------------------------------------------------------------------------------

# filename = "my5repos-public.json"

# url = 'https://api.github.com/users/nurbujang/repos?per_page=100'

# response = requests.get(url)
# print (response.status_code) # make sure u get 200
# repoJSON = response.json() # turn into json
# #print (response.json())

# with  open(filename, 'w') as fp: # save into file called my5repos-public.json
#     json.dump(repoJSON, fp, indent=4)
#------------------------------------------------------------------------------------

# copy the contents_url https://api.github.com/repos/nurbujang/WSAA-coursework/contents/{+path}

# filename = "my5repos-public.json"

# url = 'https://api.github.com/repos/nurbujang/WSAA-coursework/contents/{+path}'

# response = requests.get(url)
# print (response.status_code) # make sure u get 200
# repoJSON = response.json() # turn into json
# #print (response.json())

# with  open(filename, 'w') as fp: # save into file called my5repos-public.json
#     json.dump(repoJSON, fp, indent=4)

#---------------------------------------------------------------------------
# lets say u want to see the contents of lab:

filename = "my5repos-wsaa-labs.json"

url = 'https://api.github.com/repos/nurbujang/WSAA-coursework/contents/labs'

response = requests.get(url)
print (response.status_code) # make sure u get 200
repoJSON = response.json() # turn into json
#print (response.json())

with  open(filename, 'w') as fp: # save into file called my5repos-wsaa-labs.json
    json.dump(repoJSON, fp, indent=4)

####################################################################
    # GET INFO FROM Private REPO: >>> my5getprivaterepository.py








# #filename = "repos-public.json"
# filename = "wsaa-code.json"

# #url = 'https://api.github.com/users/andrewbeattycourseware/repos?per_page=100'
# url = 'https://api.github.com/repos/andrewbeattycourseware/wsaa-course-material/contents/code'
# #url = 'https://api.github.com/repos/andrewbeattycourseware/aprivateone'

# response = requests.get(url)
# print (response.status_code)
# repoJSON = response.json()
# #print (response.json())

# with  open(filename, 'w') as fp:
#     json.dump(repoJSON, fp, indent=4)
