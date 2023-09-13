theList = [ 1,3,5,7,9 ]

def adder(theList):
    temp = 0
    for i in range(len(theList)):
        temp = temp + theList[i]
    print(temp)
adder(theList)
def productFinder(list):
    temp = 1
    for i in range(len(list)):
        temp = temp * list[i]
    return temp
print(productFinder(theList))