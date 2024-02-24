# converts a web page to a pdf 
# This is to demonstrate API Keys
# Author: Andrew Beatty

# import requests
# import urllib.parse

# targetUrl = "https://en.wikipedia.org"
# #targetUrl = "https://www.atu.ie/"

# apikey = "ljWKVtWMmaQaPkq8wJZ3Es22W2MRnf2c9R5fK8QE7f5cjiJgDW6GJ6AQk7yh7J6k"
# apiurl = 'https://api.html2pdf.app/v1/generate'

# params = {'html': targetUrl,'apiKey': apikey}
# parsedparams = urllib.parse.urlencode(params)

# requestUrl = apiurl +"?" + parsedparams 
# print (requestUrl)  # just for debugging

# response = requests.get(requestUrl)

# print (response.status_code)
# result =response.content

# with open("my5document.pdf", "wb") as handler:
#     handler.write(result)

# my5document.pdf, my5config,py, then below:

import requests
import urllib.parse
from config import apikeys as cfg

targetUrl = "https://en.wikipedia.org"
#targetUrl = "https://www.atu.ie/"

apikey = cfg["htmltopdfkey"]
apiurl = 'https://api.html2pdf.app/v1/generate'

params = {'html': targetUrl,'apiKey': apikey}
parsedparams = urllib.parse.urlencode(params)

requestUrl = apiurl +"?" + parsedparams 
print (requestUrl)  # just for debugging

response = requests.get(requestUrl)

print (response.status_code)
result =response.content

with open("my5document.pdf", "wb") as handler:
    handler.write(result)


# import requests
# import urllib.parse
# from config import apikeys as cfg

# targetUrl = "https://en.wikipedia.org"
# #targetUrl = "https://www.atu.ie/"

# apikey = cfg["htmltopdfkey"]
# apiurl = 'https://api.html2pdf.app/v1/generate'

# params = {'html': targetUrl,'apiKey': apikey}
# parsedparams = urllib.parse.urlencode(params)

# requestUrl = apiurl +"?" + parsedparams 
# print (requestUrl)

# response = requests.get(requestUrl)

# print (response.status_code)
# result =response.content

# with open("document.pdf", "wb") as handler:
#     handler.write(result)