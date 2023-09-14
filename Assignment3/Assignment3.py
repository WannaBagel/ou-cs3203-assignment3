from itertools import product



def adder(theList):
    temp = 0
    for i in range(len(theList)):
        temp = temp + theList[i]
    return(temp)
def productFinder(list):
    temp = 1
    for i in range(len(list)):
        temp = temp * list[i]
    return temp
def main():
    print("Welcome to assignment 3 \n")
    ourList = []
    while True:
        userInput = input("Insert a number, or 'Stop' to end \n")
        
        if userInput.lower() == "stop":
            break
        
        try:
            number = int(userInput)
            ourList.append(number)
        except ValueError:
            print("Invalid input. Please enter a valid number or 'stop' to stop. \n")
    user_choice = input("Type 'Adder' for addition or 'mult' for multiplication.' \n")
    
    print(adder(ourList))
    print(productFinder(ourList))
    
        
main()