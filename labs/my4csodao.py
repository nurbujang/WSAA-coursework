# cso.ie > datasets > data.cso.ie - CSO's PxStat Open data Statistical Database
# pick one > -API Data Query > Restful Api > Copy url (ends with en)
# https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FP004/JSON-stat/2.0/en



# as rough and ready module for accessing CSO data that is in the pxstat format
# Work needs to be done to this to allow it to read data sets of N dimensions
# Author: Andrew Beatty

from ast import Pass
import requests
import json

# https://data.cso.ie/ > browse > people and Society > 
# in Search: Preliminary Actual and Percentage Change in Population 2016 - 2022 FP001
# API Data QUery > Restful > copy url which ends with JSON-stat/2.0/en
# https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FP001/JSON-stat/2.0/en

# url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FP001/JSON-stat/2.0/en"

# def getAll():
#     Pass

# if __name__ == "__main__":
#     print("hello")

#------------------------------------------------
    
# url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FP001/JSON-stat/2.0/en"

# def getAll():
#     response = requests.get(url)
#     return response.json()

# if __name__ == "__main__":
#     with open("my4cso.json", "wt") as fp:
#         print(json.dumps(getAll()), file=fp)

#--------------------------------# IN ASSIGNMENT 3
# FP001 is a particular data set. It would be really cool if I could get that data set. 

# urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/" # note: leave the / at the end
# urlEnd = "/JSON-stat/2.0/en" # delete FP001

# def getAll(dataset): # pass in the dataset here
#     url=urlBeginning + dataset + urlEnd
#     response = requests.get(url)
#     return response.json()

# if __name__ == "__main__":
#     with open("my4cso.json", "wt") as fp:
#         print(json.dumps(getAll("FP001")), file=fp)

#---------------------------------------------------------
# we will use this a lot

# urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
# urlEnd = "/JSON-stat/2.0/en" # delete FP001

# def getAllAsFile(dataset): 
#     with open("my4cso.json", "wt") as fp:
#         print(json.dumps(getAll(dataset)), file=fp)

# def getAll(dataset): 
#     url=urlBeginning + dataset + urlEnd
#     response = requests.get(url)
#     return response.json()

# if __name__ == "__main__":
#     getAllAsFile("FP001")

#-----------------------------------------------------------------
#So I want to do some analysis on this so I could put it into a separate file if I wanted to. 
#In one sense, I feel I'm going to be reusing the code to basically make it
# in my way, passed, to make something that looks easy to iterate like result.json

# urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
# urlEnd = "/JSON-stat/2.0/en" # delete FP001

# def getAllAsFile(dataset): 
#     with open("my4cso.json", "wt") as fp:
#         print(json.dumps(getAll(dataset)), file=fp)

# def getAll(dataset): 
#     url=urlBeginning + dataset + urlEnd
#     response = requests.get(url)
#     return response.json()

# def getFormattedAsFile(dataset): # to make it quicker and easier, bc there's a lot of data
#     pass

# def getFormatted(dataset):
#     data = getAll(dataset)
#     ids = data["id"] # get all the ids from my4cso.json
#     values = data["value"]# get values
#     dimensions = data ["dimension"] #get dimensions
#     sizes = data ["size"]

#     for id in ids:
#         print(id) #check if it works

# if __name__ == "__main__":
#     #getAllAsFile("FP001")
#     getFormatted("FP001")

# will get results from output: STATISTIC, TLIST, c02199v02655, c03788v04538
    
#-------------------------------------------------
# now what I need to do is I need to go through 4 different 4 loops to unpack all the data.
    # GO TO SIZE IN m4cso.json, size has 4 dimensions [4, 1, 3, 27]

# urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
# urlEnd = "/JSON-stat/2.0/en" # delete FP001

# def getAllAsFile(dataset): 
#     with open("my4cso.json", "wt") as fp:
#         print(json.dumps(getAll(dataset)), file=fp)

# def getAll(dataset): 
#     url=urlBeginning + dataset + urlEnd
#     response = requests.get(url)
#     return response.json()

# def getFormattedAsFile(dataset): # to make it quicker and easier, bc there's a lot of data
#     pass

# def getFormatted(dataset):
#     data = getAll(dataset)
#     ids = data["id"] # get all the ids from my4cso.json
#     values = data["value"]# get values
#     dimensions = data ["dimension"] #get dimensions
#     sizes = data ["size"]

#     for dim1 in range(0, sizes[0]): # element 0 is 4
#         currentId = ids[0] # from the dimension > statistic > category> get all 4 index and their label
#         print(currentId) # test

# if __name__ == "__main__":
#     #getAllAsFile("FP001")
#     getFormatted("FP001")

# will get results from output: STATISTIC, STATISTIC, STATISTIC, STATISTIC

#--------------------------------------------------------------------

# urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
# urlEnd = "/JSON-stat/2.0/en" # delete FP001

# def getAllAsFile(dataset): 
#     with open("my4cso.json", "wt") as fp:
#         print(json.dumps(getAll(dataset)), file=fp)

# def getAll(dataset): 
#     url=urlBeginning + dataset + urlEnd
#     response = requests.get(url)
#     return response.json()

# def getFormattedAsFile(dataset): # to make it quicker and easier, bc there's a lot of data
#     pass

# def getFormatted(dataset):
#     data = getAll(dataset)
#     ids = data["id"] # get all the ids from my4cso.json
#     values = data["value"]# get values
#     dimensions = data ["dimension"] #get dimensions
#     sizes = data ["size"]

#     for dim1 in range(0, sizes[0]): # element 0 is 4
#         currentId = ids[0] # from the dimension > statistic > category> get all 4 index and their label
#         index = dimensions[currentId]["category"]["index"][dim1]
#         label = dimensions[currentId]["category"]["label"][index]
#         print(label) # test

# if __name__ == "__main__":
#     #getAllAsFile("FP001")
#     getFormatted("FP001")

# # output: 
# # Population 2016
# Population 2022
# Actual change since previous census
# Percentage change since previous census
    
#--------------------------------------------------------------
# So that's the first dimension. 
# Now I need to do the same for the 2nd dimension. I'm going to do this four times. 

# urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
# urlEnd = "/JSON-stat/2.0/en" # delete FP001

# def getAllAsFile(dataset): 
#     with open("my4cso.json", "wt") as fp:
#         print(json.dumps(getAll(dataset)), file=fp)

# def getAll(dataset): 
#     url=urlBeginning + dataset + urlEnd
#     response = requests.get(url)
#     return response.json()

# def getFormattedAsFile(dataset): # to make it quicker and easier, bc there's a lot of data
#     pass

# def getFormatted(dataset):
#     data = getAll(dataset)
#     ids = data["id"] # get all the ids from my4cso.json
#     values = data["value"]# get values
#     dimensions = data ["dimension"] #get dimensions
#     sizes = data ["size"]

# # do this four times. 
#     for dim0 in range(0, sizes[0]): # element 0 is 4
#         currentId = ids[0] # from the dimension > statistic > category> get all 4 index and their label
#         index = dimensions[currentId]["category"]["index"][dim0]
#         label = dimensions[currentId]["category"]["label"][index]
#         print(label) # test
         
#         for dim1 in range(0, sizes[1]): # element 1
#             currentId = ids[1] # tlist(A1), category, index (only 1 dimension) and its label,
#             index = dimensions[currentId]["category"]["index"][dim1]
#             label = dimensions[currentId]["category"]["label"][index]
#             print("\t",label) # test
            
#             for dim2 in range(0, sizes[2]): # element 2
#                 currentId = ids[2] # C02199v02655, category, index (has 3 dimensions(both sexes, male, female)) and label
#                 index = dimensions[currentId]["category"]["index"][dim2]
#                 label = dimensions[currentId]["category"]["label"][index]
#                 print("\t\t",label) # test
#                 for dim3 in range(0, sizes[3]): # element 3
#                     currentId = ids[3] # 
#                     index = dimensions[currentId]["category"]["index"][dim3]
#                     label = dimensions[currentId]["category"]["label"][index]
#                     print("\t\t\t",label) # test

# if __name__ == "__main__":
#     #getAllAsFile("FP001")
#     getFormatted("FP001")

# # output: 
# both sexes, male, female in each county
    
#----------------------------------------------------------
# now we need to count the values as we go

# urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
# urlEnd = "/JSON-stat/2.0/en" # delete FP001

# def getAllAsFile(dataset): 
#     with open("my4cso.json", "wt") as fp:
#         print(json.dumps(getAll(dataset)), file=fp)

# def getAll(dataset): 
#     url=urlBeginning + dataset + urlEnd
#     response = requests.get(url)
#     return response.json()

# def getFormattedAsFile(dataset): # to make it quicker and easier, bc there's a lot of data
#     pass

# def getFormatted(dataset):
#     data = getAll(dataset)
#     ids = data["id"] # get all the ids from my4cso.json
#     values = data["value"]# get values
#     dimensions = data ["dimension"] #get dimensions
#     sizes = data ["size"]
#     valuecount = 0

# # do this four times. 
#     for dim0 in range(0, sizes[0]): # element 0 is 4
#         currentId = ids[0] # from the dimension > statistic > category> get all 4 index and their label
#         index = dimensions[currentId]["category"]["index"][dim0]
#         label = dimensions[currentId]["category"]["label"][index]
#         print(label) # test
         
#         for dim1 in range(0, sizes[1]): # element 1
#             currentId = ids[1] # tlist(A1), category, index (only 1 dimension) and its label,
#             index = dimensions[currentId]["category"]["index"][dim1]
#             label = dimensions[currentId]["category"]["label"][index]
#             print("\t",label) # test
            
#             for dim2 in range(0, sizes[2]): # element 2
#                 currentId = ids[2] # C02199v02655, category, index (has 3 dimensions(both sexes, male, female)) and label
#                 index = dimensions[currentId]["category"]["index"][dim2]
#                 label = dimensions[currentId]["category"]["label"][index]
#                 print("\t\t",label) # test
#                 for dim3 in range(0, sizes[3]): # element 3
#                     currentId = ids[3] # 
#                     index = dimensions[currentId]["category"]["index"][dim3]
#                     label = dimensions[currentId]["category"]["label"][index]
#                     print("\t\t\t",label, " ", values[valuecount]) # test
#                     valuecount += 1

# if __name__ == "__main__":
#     #getAllAsFile("FP001")
#     getFormatted("FP001")

# output: for both sexes, male and female, county and count for each county
    
    #----------------------------------------------------------
# so that's it printed out in a nice way. 
# I would like to put this into some kind of nice dict
# so I could save this out and then I could analyse it.

# urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
# urlEnd = "/JSON-stat/2.0/en" # delete FP001

# def getAllAsFile(dataset): 
#     with open("my4cso.json", "wt") as fp:
#         print(json.dumps(getAll(dataset)), file=fp)

# def getAll(dataset): 
#     url=urlBeginning + dataset + urlEnd
#     response = requests.get(url)
#     return response.json()

# def getFormattedAsFile(dataset): # to make it quicker and easier, bc there's a lot of data
#     pass

# def getFormatted(dataset):
#     data = getAll(dataset)
#     ids = data["id"] # get all the ids from my4cso.json
#     values = data["value"]# get values
#     dimensions = data ["dimension"] #get dimensions
#     sizes = data ["size"]
#     valuecount = 0
#     result = {} # empty dictionary object
#     currentDict = result

# # do this four times. 
#     for dim0 in range(0, sizes[0]): # element 0 is 4
#         currentId = ids[0] # from the dimension > statistic > category> get all 4 index and their label
#         index = dimensions[currentId]["category"]["index"][dim0]
#         label = dimensions[currentId]["category"]["label"][index]
#         result[label]={} # instead of printing put the label, equal to printing out a new object
#         currentDict[label]={} 
#         currentDict = currentDict[label]
#         #So what I'm doing is always shifting up the current dictionary to be.
#         #That should be shifting it up to be its sub object each time.
#         # The reason I'm doing it this way is so that I can later on make this generic for any amount of dimensions.
#         for dim1 in range(0, sizes[1]): # element 1
#             currentId = ids[1] # tlist(A1), category, index (only 1 dimension) and its label,
#             index = dimensions[currentId]["category"]["index"][dim1]
#             label = dimensions[currentId]["category"]["label"][index]
#             currentDict[label]={}
#             currentDict = currentDict[label]
#             for dim2 in range(0, sizes[2]): # element 2
#                 currentId = ids[2] # C02199v02655, category, index (has 3 dimensions(both sexes, male, female)) and label
#                 index = dimensions[currentId]["category"]["index"][dim2]
#                 label = dimensions[currentId]["category"]["label"][index]
#                 currentDict[label]={}
#                 currentDict = currentDict[label]
#                 for dim3 in range(0, sizes[3]): # element 3
#                     currentId = ids[3] # 
#                     index = dimensions[currentId]["category"]["index"][dim3]
#                     label = dimensions[currentId]["category"]["label"][index]
#                     #print("\t\t\t",label, " ", values[valuecount]) # test
#                     currentDict[label]=values[valuecount]
#                     valuecount += 1

#         # when done, put into a file, but test first
#         print(result)
#         return result


# if __name__ == "__main__":
#     #getAllAsFile("FP001")
#     getFormatted("FP001")

# output: 
    
#============================================
# now put into a file
# so I could save this out and then I could analyse it.

urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/" # note: leave the / at the end
urlEnd = "/JSON-stat/2.0/en" # delete FP001

def getAllAsFile(dataset): 
    with open("my4cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

def getAll(dataset): 
    url=urlBeginning + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getFormattedAsFile(dataset): # to make it quicker and easier, bc there's a lot of data
    with open("my4cso-formatted.json", "wt") as fp:
        print(json.dumps(getFormatted(dataset)), file=fp)

def getFormatted(dataset):
    data = getAll(dataset)
    ids = data["id"] # get all the ids from my4cso.json
    values = data["value"]# get values
    dimensions = data ["dimension"] #get dimensions
    sizes = data ["size"]
    valuecount = 0
    result = {} # empty dictionary object
    
# do this four times. 
    for dim0 in range(0, sizes[0]): # element 0 is 4
        currentId = ids[0] # from the dimension > statistic > category> get all 4 index and their label
        index = dimensions[currentId]["category"]["index"][dim0]
        label0 = dimensions[currentId]["category"]["label"][index]
        result[label0]={} # instead of printing put the label, equal to printing out a new object
        #So what I'm doing is always shifting up the current dictionary to be.
        #That should be shifting it up to be its sub object each time.
        # The reason I'm doing it this way is so that I can later on make this generic for any amount of dimensions.
        print(label0)
        for dim1 in range(0, sizes[1]): # element 1
            currentId = ids[1] # tlist(A1), category, index (only 1 dimension) and its label,
            index = dimensions[currentId]["category"]["index"][dim1]
            label1 = dimensions[currentId]["category"]["label"][index]
            #print("\t",label1)
            result[label0][label1]={} # equal to new object
            for dim2 in range(0, sizes[2]): # element 2
                currentId = ids[2] # C02199v02655, category, index (has 3 dimensions(both sexes, male, female)) and label
                index = dimensions[currentId]["category"]["index"][dim2]
                label2 = dimensions[currentId]["category"]["label"][index]
                result[label0][label1][label2]={} # equal to new object
                #print("\t\t",label2)
                for dim3 in range(0, sizes[3]): # element 3
                    currentId = ids[3] # 
                    index = dimensions[currentId]["category"]["index"][dim3]
                    label3 = dimensions[currentId]["category"]["label"][index]
                    #print("\t\t\t",label, " ", values[valuecount]) # test
                    result[label0][label1][label2][label3]=values[valuecount] # equal to new object
                    valuecount += 1

        # when done, put into a file, but test first
        
    return result # this tab indentation is important or else it will cut off to 2016 only


if __name__ == "__main__":
    #getAllAsFile("FP001")
    getFormattedAsFile("FP001")

# output: 


#######################################################################################

# urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
# urlEnd = "/JSON-stat/2.0/en"

# def getAllAsFile(dataset):
#     with open("cso.json", "wt") as fp:
#         print(json.dumps(getAll(dataset)), file=fp)

# def getAll(dataset):   
#     url = urlBegining + dataset + urlEnd
#     response = requests.get(url)
#     return response.json()

# def getFormattedAsFile(dataset):
#     with open("cso-formatted.json", "wt") as fp:
#         print(json.dumps(getFormatted(dataset)), file=fp)
  

# def getFormatted(dataset):
#     data = getAll(dataset)
#     ids = data["id"]
#     values = data["value"]
#     dimensions = data["dimension"]
#     sizes = data["size"]
#     valuecount = 0
#     result = {}
    
#     for dim0 in range(0, sizes[0]):
#         currentId = ids[0]
#         index = dimensions[currentId]["category"]["index"][dim0]
#         label0 = dimensions[currentId]["category"]["label"][index]
#         result[label0]={}
        
#         print(label0)
#         for dim1 in range(0, sizes[1]):
#             currentId = ids[1]
#             index = dimensions[currentId]["category"]["index"][dim1]
#             label1 = dimensions[currentId]["category"]["label"][index]
#             #print("\t",label1)
#             result[label0][label1]={}
#             for dim2 in range(0, sizes[2]):
#                 currentId = ids[2]
#                 index = dimensions[currentId]["category"]["index"][dim2]
#                 label2 = dimensions[currentId]["category"]["label"][index]
#                 #print("\t\t",label2)
#                 result[label0][label1][label2]={}
           
#                 for dim3 in range(0, sizes[3]):
#                     currentId = ids[3]
#                     index = dimensions[currentId]["category"]["index"][dim3]
#                     label3 = dimensions[currentId]["category"]["label"][index]
#                     #print("\t\t\t",label, " ", values[valuecount])
#                     result[label0][label1][label2][label3]= values[valuecount]
#                     valuecount+=1

        
#     return result
    


# if __name__ == "__main__":
#     #getAllAsFile("FP001")
#     getFormattedAsFile("FP001")