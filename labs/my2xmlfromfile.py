from xml.dom.minidom import parse

filename = "employees.xml"

# read file in two ways
doc = parse(filename)
# or
#with open(filename) as fp:
#    doc = parse(fp)

# to check if it works:
#print (doc.toprettyxml(), end='') # output to console
print (doc.toprettyxml(newl=''))

emloyeeNodeList = doc.getElementsByTagName("Employee")
print(len(emloyeeNodeList))
for employeeNode in emloyeeNodeList:
    #print("->")
    firstNameNode = employeeNode.getElementsByTagName("FirstName").item(0)
    firstName = firstNameNode.firstChild.nodeValue.strip()
    print (firstName)