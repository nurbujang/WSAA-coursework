# This is a module that provides a set of functions to interact with
# the demonstration book API hosted at PythonAnyhwere
# Author Andrew Beatty

import requests
import json
url = "http://andrewbeatty1.pythonanywhere.com/books"

def getAllBooks():
    response = requests.get(url)
    return response.json()

# if __name__ == "__main__": #test
#     print(getAllBooks())

def getBookById(id): # to get 1 book
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

# if __name__ == "__main__": #test
#     print(getBookById(197))


def deleteBook(id): # to delete book is easy
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

# if __name__ == "__main__": #test
#     print(deleteBook(197))

#----------------------------------
#Method 1 create book
#def createBook(book): # to  create a post (create a book)
    #pass
    # book = {
    #     'Author':"test",
    #     'Title':"test",
    #     'Price':123
    # }
    # #response = requests.post(url,json=json.dumps(book)) # method 1, convert dict object into a string, not prefered
    # return response.json()
# if error, go to postman, post, header is application/json, send

# def createBook(book): # to  create a post (create a book)
#     book = {
#         'Author':"test2",
#         'Title':"test2",
#         'Price':1232
#     }
#     response = requests.post(url,json=book) # PREFERRED
#     return response.json()

# if __name__ == "__main__": #test
#     print(createBook({}))

# Method 2 create book, more complicated
# def createBook(book): # to  create a post (create a book)
#     book = {
#         'Author':"test3",
#         'Title':"test3",
#         'Price':12323
#     }
#     headers ={ "Content-type": "application/json"}
#     response = requests.post(url, data=json.dumps(book), headers=headers)
#     return response.json()

# if __name__ == "__main__": #test
#     print(createBook({}))

# ----------------------------------
# def createBook(book): # to  create a post (create a book)

#     response = requests.post(url,json=book) # PREFERRED
#     return response.json()

# if __name__ == "__main__": #test
#     book = {
#         'Author':"test4",
#         'Title':"test4",
#         'Price':123234
#     }
#     print(createBook(book))

# -------------

def updateBook(id, bookdiff): # pass in what's different in a book
    #pass
    updateurl = url + "/" + str(id)
    response = requests.put(updateurl, json=bookdiff)
    return response.json()

if __name__ == "__main__":
    book= {
        'Author':"test",
        'Title':"test title",
        "Price": 123
    }
    bookdiff= {
        "Price": 100000000
    }
    print (updateBook(493, bookdiff))







##################################################################
# import requests
# import json
# url = "http://andrewbeatty1.pythonanywhere.com/books"

# def getAllBooks():
#     response = requests.get(url)
#     return response.json()

# def getBookById(id):
#     geturl = url + "/" + str(id)
#     response = requests.get(geturl)
#     return response.json()

# def createBook(book):
    
#     response = requests.post(url, json=book)
#     #headers ={ "Content-type": "application/json"}
#     #response = requests.post(url, data=json.dumps(book), headers=headers)
    
#     return response.json()


# def updateBook(id, bookdiff):
#     updateurl = url + "/" + str(id)
#     response = requests.put(updateurl, json=bookdiff)
#     return response.json()
#     pass

# def deleteBook(id):
#     deleteurl = url + "/" + str(id)
#     response = requests.delete(deleteurl)
#     return response.json()
   

# if __name__ == "__main__":
#     book= {
#         'Author':"test",
#         'Title':"test title",
#         "Price": 123
#     }
#     bookdiff= {
#         "Price": 1234444
#     }
#     #print(getAllBooks())
#     print(getBookById(22))
#     #print (deleteBook(76))
#     #print (deleteBook(81))
#     #print (createBook(book))
#     print (updateBook(22, bookdiff))