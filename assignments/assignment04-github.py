'''
Assignment 4 for Web Services and Applications (Spring 2024)
assignment04-github.py
Author: Nur Bujang

Write a program in python that will read a file from a repository. 
The program should then replace all the instances of the text "Andrew" with your name. 

The program should then commit those changes and push the file back to the repository (You will need authorisation to do this).
I do not need to see your keys (see lab2, to follow)

Handup: Push the program as assignment04-github.py to assignments repository.
Marks: Marks will be given for the functionality and layout of the code; I do expect minimal comments to indicate you know what the program is doing.

'''

# private repository is nurbujang/private, filename is andrew.txt
# using PyGitHub is a Python library (Jacques, 2024)
# code from Beatty (2024)

from github import Github
import requests
from config import config as cfg 

apikey = cfg["githubkey"] # contained in config.py

g = Github(apikey) 

repo = g.get_repo("nurbujang/private")
#print(repo.clone_url) # print url of repository

fileInfo = repo.get_contents("andrew.txt") # used in the PyGithub library to fetch the contents of a file from a repository (pygithub.readthedocs.io, n.d.)
urlOfFile = fileInfo.download_url  # extract the download URL of the file from the ContentOfFile object from andrew.txt
#print (urlOfFile) # print the download URL of the file

response = requests.get(urlOfFile) # requests library to perform HTTP GET requests and returns a response object which contains the response from the server (GeeksforGeeks, 2020)
contentOfFile = response.text # retrieves the textual content of the response obtained from the HTTP request
#print (contentOfFile) # print original content before replacement

# Replace Andrew with Nur and keep adding new line to replace
# replace using python treing replace() method (www.w3schools.com, n.d.)
newContents = contentOfFile.replace("Andrew", "Nur")  + " next to replace: Andrew andrew Andrw ANdr Andrww ndrew wander andwww Adrew Anrew andrrw anddrw Adder Anddrew Andww andrew Andrew \n"
print (newContents)

# update_file(path, message, content, sha, branch=NotSet, committer=NotSet, author=NotSet) (Beatty, 2024)
gitHubResponse=repo.update_file(fileInfo.path,"update Andrew to Nur and add new",newContents,fileInfo.sha)
print (gitHubResponse)


'''
REFERENCES

Beatty, A. (2024). andrewbeattycourseware/wsaa-course-material. [online] GitHub. Available at: https://github.com/andrewbeattycourseware/wsaa-course-material [Accessed 26 Feb. 2024].
GeeksforGeeks. (2020). GET method - Python requests. [online] Available at: https://www.geeksforgeeks.org/get-method-python-requests/ [Accessed 26 Feb. 2024].
Jacques, V. (2024). PyGithub: Use the full Github API v3. [online] PyPI. Available at: https://pypi.org/project/PyGithub/ [Accessed 25 Feb. 2024].
pygithub.readthedocs.io. (n.d.). Repository — PyGithub 2.2.1.dev3+gaf529ab documentation. [online] Available at: https://pygithub.readthedocs.io/en/latest/examples/Repository.html [Accessed 26 Feb. 2024].
www.w3schools.com. (n.d.). Python String replace() Method. [online] Available at: https://www.w3schools.com/python/ref_string_replace.asp [Accessed 26 Feb. 2024].
_______________________________________________________________________________________________
End
'''