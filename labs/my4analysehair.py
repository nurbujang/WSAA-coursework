# the 2nd part

# from my4valoffdao import getAll

# data = getAll()

# for entry in data:
#     print(entry) # will  print all. get valuationreport from here.
    
#----------------------------------
# from my4valoffdao import getAll

# data = getAll()

# for entry in data:
#     #print(entry) # will  print all. get valuationreport from here.
#     valuationReports = entry["ValuationReport"]
#     print(valuationReports)

#--------------------------------------

# from my4valoffdao import getAll

# data = getAll()

# for entry in data:
#     #print(entry) # will  print all. get valuationreport from here.
#     valuationReports = entry["ValuationReport"]
#     #print(valuationReports)
#     for valuationReport in valuationReports:
#         print(valuationReport)

#-------------------------------------------
# So now I need to look at the floor use and if the floor use is a hair salon,    
          
from my4valoffdao import getAll

data = getAll()
totalArea = 0
for entry in data:
    #print(entry) # will  print all. get valuationreport from here.
    valuationReports = entry["ValuationReport"]
    #print(valuationReports)
    for valuationReport in valuationReports:
        #print(valuationReport)
        if valuationReport["FloorUse"] == "HAIR SALON":
            totalArea += valuationReport["Area"]
print (totalArea)
# to double check, go to json, Crtl+F, type hair, do math. 215.21 is correct

#------------------------------------------------------------------
# ROUNDING ERROR results with many decimal places eg: 318.7899999999996 bc it's adding floating point numbers
# NEVER USE FLOATING POINT NUMBERS WHEN ADDING UP

from my4valoffdao import getAll

data = getAll()
totalArea = 0
for entry in data:
    #print(entry) # will  print all. get valuationreport from here.
    valuationReports = entry["ValuationReport"]
    #print(valuationReports)
    for valuationReport in valuationReports:
        #print(valuationReport)
        if valuationReport["FloorUse"] == "HAIR SALON":
            print(valuationReport["Area"],"+", totalArea,"=", end="") # end=nothing
            totalArea += valuationReport["Area"]
            print (totalArea)
print (totalArea)

# still rounding error
# open mymessing.py

#########################################################################
# from webbrowser import get
# from my4valoffdao import getAll

# data = getAll()
# totalArea = 0
# for entry in data:
#     valuationReports = entry["ValuationReport"]
#     #print(valuationReports)
#     for valuationReport in valuationReports:
#         #print(valuationReport)
#         #if valuationReport["FloorUse"] == "HAIR SALON":
#             #print (valuationReport["Area"],"+", totalArea,"=", end="")
#         totalArea += valuationReport["Area"]
#             #print(totalArea)

# print (totalArea)

# OTHERS:
# DATA.GOV >accomodation > preview > copy url on Resource: Accommodations CSV.> open and save

#URL: https://failteireland.azure-api.net/opendata-api/v1/accommodation/csv

#or Accomodation Api > go to Resource

# met eirann are all xml > preview

