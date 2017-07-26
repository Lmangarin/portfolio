import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)
# print the first element

# print the last element
#print(elementsList[len(elementsList)-1])
# print all the elements
for element in elementsList:
    print (">", element)

# Start your search algorithm here.
print ("==>Remember: List is case sensitive!!<==")
CountryIWant = input("What country do you want to choose?? \n>>")
beginningIndex = 0
endingIndex = len(elementsList)-1
index = int((endingIndex-beginningIndex)/2)
while elementsList[index] != CountryIWant:
    if CountryIWant < elementsList[index]:
        beginningIndex = beginningIndex
        endingIndex = index
        index = int((endingIndex-beginningIndex)/2)+ beginningIndex
    elif CountryIWant > elementsList[index]:
        beginningIndex = index+1
        endingIndex = endingIndex
        index = int((endingIndex-beginningIndex)/2)+ beginningIndex
    else:
        print (index)
print ("The value is: ",index)
print ("Index were: ","B",beginningIndex, "M", index, "E",endingIndex)
