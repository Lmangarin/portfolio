#Function to add numbers in the given list
def add (number_list):
    result = 0
    for number in number_list:
        result = result + int(number)
    return result

#Function to find the average of numbers in the given list
def average(number_list):
    result = 0
    listsum = 0
    listlength = len(number_list)
    listsum = add(number_list)
    result = listsum/listlength
    return result

#Our main program starts here

answer = 0

option = input("Do you want to add or find an average? add/average ")
if option != "add" and option != "average":
    print ("Invalid option")
    exit()


numbersIn = input ("Enter numbers separated by comma: ")

numberslist = numbersIn.split(",")

if option == "add":
    answer = add(numberslist)
elif option == "average":
    answer = average(numberslist)
print ("The answer is:", answer)
