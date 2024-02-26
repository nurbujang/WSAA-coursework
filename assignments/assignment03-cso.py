'''
Assignment 3 for Web Services and Applications (Spring 2024)
assignment03-cso.py
Author: Nur Bujang

Write a program that retrieves the dataset for the "exchequer account (historical series)" from the CSO, 
and stores it into a file called "cso.json".

https://www.cso.ie/en/index.html

Link to a CSO dataset that will help you with the assignment:
https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en

    Upload this program to the same repository you used for the XML assignment
    Save this assignment as "assignment03-cso.py"
    This program should not be a long one
        I don't need you to reformat or analyse the data in any way
        It should be about 10ish lines long (I have not counted)
    You will need to find the dataset in CSO.ie, try economic and then finance, then finance indicators. 
    Yes it is difficult to find, that is part of the task, actually the easiest way to find it is search for it.

Save your program in the repository you used for the first assignment (I will be correcting all these at the end of the semester)
You do not need to over comment your code.

'''
# Steps:
# https://www.cso.ie/en/index.html > https://www.cso.ie/en/databases/ 
# > Other Public Sector Databases > Revenue Tax and Customs Statistics
# Search: exchequer account (historical series)
# url = https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en # Data.cso.ie (2020)

import requests
import json

urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/" # be sure to leave the /
urlEnd = "/JSON-stat/2.0/en"

def getAll(dataset): # Beatty (2024)
    url= urlBeginning + dataset + urlEnd
    response = requests.get(url) # get() function retrieves the resource specified by the URL and returns a response object containing the response from the server (GeeksforGeeks, 2020b)
    return response.json() # json() method of the response object parses the response content as JSON and returns it as a Python dictionary or list (GeeksforGeeks, 2020a)

if __name__ == "__main__": # execute code when file runs as a script (Breuss, n.d.)
    with open("cso.json", "wt") as fp: # with open, "w" is write mode (note.nkmk.me, 2023)
        print(json.dumps(getAll("FIQ02")), file=fp) # pass in the dataset FIQ02 here

'''
REFERENCES

Beatty, A. (2024). andrewbeattycourseware/wsaa-course-material. [online] GitHub. Available at: https://github.com/andrewbeattycourseware/wsaa-course-material [Accessed 19 Feb. 2024].
Breuss, M. (n.d.). What Does if __name__ == ‘__main__’ Do in Python? – Real Python. [online] realpython.com. Available at: https://realpython.com/if-name-main-python/ [Accessed 19 Feb. 2024].
Data.cso.ie. (2020). FIQ02 Exchequer Account (Historical Series). [online] Available at: https://data.cso.ie/ [Accessed 19 Feb. 2024].
GeeksforGeeks. (2020a). response.json() - Python requests. [online] Available at: https://www.geeksforgeeks.org/response-json-python-requests/ [Accessed 19 Feb. 2024].
GeeksforGeeks. (2020b). response.url - Python requests. [online] Available at: https://www.geeksforgeeks.org/response-url-python-requests/ [Accessed 19 Feb. 2024].
note.nkmk.me. (2023). Read, write, and create files in Python (with and open()) | note.nkmk.me. [online] Available at: https://note.nkmk.me/en/python-file-io-open-with/#open-a-file-for-writing-modew [Accessed 19 Feb. 2024].
_______________________________________________________________________________________________
End
'''