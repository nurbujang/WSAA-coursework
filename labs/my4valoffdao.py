# Question: How many sq ft. of hair salons there are in Co. Wicklow?
# https://api.valoff.ie/ > select filters 
# http://localhost:4974/api/Property/GetProperties?Fields=LocalAuthority%2CCategory%2CLevel%2CAreaPerFloor%2CNavTotal%2CCarPark%2CPropertyNumber%2CIG%2CUse%2CFloorUse%2CAddress%2CPublicationDate&LocalAuthority=WICKLOW%20COUNTY%20COUNCIL&CategorySelected=OFFICE&Format=csv&Download=false
# change to:
# https://api.valoff.ie/api/Property/GetProperties?Fields=LocalAuthority%2CCategory%2CLevel%2CAreaPerFloor%2CNavTotal%2CCarPark%2CPropertyNumber%2CIG%2CUse%2CFloorUse%2CAddress%2CPublicationDate&LocalAuthority=WICKLOW%20COUNTY%20COUNCIL&CategorySelected=OFFICE&Format=csv&Download=false

# import requests
# import json

# url = "https://api.valoff.ie/api/Property/GetProperties?Fields=LocalAuthority%2CCategory%2CLevel%2CAreaPerFloor%2CNavTotal%2CCarPark%2CPropertyNumber%2CIG%2CUse%2CFloorUse%2CAddress%2CPublicationDate&LocalAuthority=WICKLOW%20COUNTY%20COUNCIL&CategorySelected=OFFICE&Format=csv&Download=false"

# def getAll():
#     response = requests.get(url)
#     return response.json()

# if __name__ == "__main__": #test
#     with open("myvaloff.json", "wt") as fp:
#         print(json.dumps(getAll()), file=fp) # json.dumps will turn it into json

#-----------------------------------------------------

#Let's mess around with this URL so I can put in different local authorities etc

# http://localhost:4974/api/Property/GetProperties?Fields=LocalAuthority%2CCategory%2CLevel%2CAreaPerFloor%2CNavTotal%2CCarPark%2CPropertyNumber%2CIG%2CUse%2CFloorUse%2CAddress%2CPublicationDate&LocalAuthority=WICKLOW%20COUNTY%20COUNCIL&CategorySelected=OFFICE&Format=json&Download=false

import requests
import json
import urllib.parse
url = "https://api.valoff.ie/api/Property/GetProperties"

parameterasDict = {
    "Download":"false",
    "Format":"json",
    "CategorySelected":"OFFICE",
    "LocalAuthority":"WICKLOW COUNTY COUNCIL",
    #"LocalAuthority":"WEXFORD COUNTY COUNCIL",
    #"LocalAuthority":"KILDARE COUNTY COUNCIL",
    "Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG%,Use,FloorUse,Address,PublicationDate"   # change %2C to ,
}

def getAll():
    parameters = urllib.parse.urlencode(parameterasDict)
    #print(parameters)
    fullurl = url + "?" + parameters
    response = requests.get(fullurl)
    return response.json()

if __name__ == "__main__": #test
    with open("myvaloff.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp) # json.dumps will turn it into json

# Then we do the analysis part (how many sqft for hair salon in my4analysehair.py)


#################################################
# import urllib.parse
# import requests
# import json
# url = "https://api.valoff.ie/api/Property/GetProperties"

# parameterasDict = {
#     "Download":"false",
#     "Format":"json",
#     "CategorySelected":"OFFICE",
#     "LocalAuthority":"WICKLOW COUNTY COUNCIL",
#     "Fields":"LocalAuthority,Category,Level,AreaPerFloor,NavTotal,CarPark,PropertyNumber,IG%,Use,FloorUse,Address,PublicationDate"   
# }

# def getAll():
#     parameters = urllib.parse.urlencode(parameterasDict)
#     #print (parameters)
#     fullurl = url + "?" + parameters
#     response = requests.get(fullurl)
#     return response.json()

# if __name__ == "__main__":
#     with open("valoff.json", "wt") as fp:
#         print(json.dumps(getAll()), file=fp)