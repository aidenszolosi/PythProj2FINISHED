#Aiden Szolosi 
#Project 4 Python
#Calculator
#Original Code Submitted @11:58
#Fixed up code following official due time 
#Project Finished 11/7/22, 1:03 AM EST

#NOTE: I do understand the policies related to late work and do understand that as this second attempt was submitted late, 
#and therefore I should not expect to receive a grade based on this code; however, I wanted to show my thinking and submit just in case my 
#changes are warranting of an exception

#PATCH NOTES FROM LAST ATTEMPT

# - Did some extended reasearch in order to try to remove any errors that may come up with the script, such as a value or syntax error
# - Try and except used to deny non numerical values when asking for the FirstNumber and SecondNumber
# - Rearranged allowedOperators into a tuple and evaluated it with in
# - *Overall, the script is far more complete and satisfies my coding OCD just a bit more as I wanted to patch the holes left 
# (Not in terms of organization as the code is a bit messy and hard to read)

allowedOperators = ("Add", "Subtract", "Multiply", "Divide")

UserInput = input("Please select one option: Add/Subtract/Multiply/Divide: ")
UserInput = str(UserInput.title())
print('You chose ' + UserInput)

#the order of variables matters here? expression didn't work as expected until switched around
if UserInput in allowedOperators: #(Is true)
    NumInput = (input("Enter the first value "))
    try:
        float(NumInput)
    except ValueError: 
        print("Unexpected Value, are you sure you entered a number? ")
        print("Please restart")
        exit() 

    FirstNumber = float(NumInput)

    NumInput2 = (input("Enter the second value "))
    try:
        float(NumInput2)
    except ValueError: 
        print("Unexpected Value, are you sure you entered a number? ")
        print("Please restart.")
        exit() 
    SecondNumber = float(NumInput2)
    
    if UserInput == "Add":
        AddedTotal = float(FirstNumber) + float(SecondNumber) 
        Equation = str(FirstNumber) + " + " + str(SecondNumber) + " = " + str(AddedTotal)
        print(Equation)
        print()
    #subtract
    elif UserInput == "Subtract":
        SubtractedTotal = float(FirstNumber) - float(SecondNumber) 
        Equation = str(FirstNumber) + " - " + str(SecondNumber) + " = " + str(SubtractedTotal)
        print(Equation)
        print()
    #multiply
    elif UserInput == "Multiply":
        MultipliedTotal = float(FirstNumber) * float(SecondNumber) 
        Equation = str(FirstNumber) + " * " + str(SecondNumber) + " = " + str(MultipliedTotal)
        print(Equation)
        print()
    #divide
    elif UserInput == "Divide":
        DividedTotal = float(FirstNumber) / float(SecondNumber) 
        Equation = str(FirstNumber) + " / " + str(SecondNumber) + " = " + str(DividedTotal)
        print(Equation)
        print()

else:
    print("Operator not recognzied")



