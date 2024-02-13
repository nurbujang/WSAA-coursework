# 9. As an exercise only store the trains whose traincode starts with a D.
# For data sets of this size, get all the data, and perform analysis (deletions) later.

import requests
import csv
from xml.dom.minidom import parseString

retrieveTags=['TrainStatus',
              'TrainLatitude',
              'TrainLongitude',
              'TrainCode',
              'TrainDate',
              'PublicMessage',
              'Direction'
              ]

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)
doc = parseString(page.content)
# check it works
# print (doc.toprettyxml(newl='')) #output to console comment this out once you know it works
# if I want to store the xml in a file. You can comment this out later
with open("lab2trainxml.xml","w") as xmlfp:
    doc.writexml(xmlfp)

# I had an issue with blank lines in the file so found solution at
# https://stackoverflow.com/questions/3348460/csv-file-written-with-python-has-blank-lines-between-each-r
# adding the newline= '' parameter
with open('week02_train.csv', mode='w', newline='') as train_file: # from mytraintimes.py
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
        traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
        traincode = traincodenode.firstChild.nodeValue.strip()
        #print (traincode)
        dataList = [] # array
        for retrieveTag in retrieveTags:
            datanode = objTrainPositionsNode.getElementsByTagName(retrieveTag).item(0)
            dataList.append(datanode.firstChild.nodeValue.strip())
        train_writer.writerow(dataList)

