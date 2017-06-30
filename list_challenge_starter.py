
from random import *


 #Create the list of words you want to choose from.
option = input("Generate a female name. Y/N ")
if option == "N":
     print ("Invalid option")
     exit()
elif option == "Y":
    word_list = ["Ileana","Loise","Heide","Marquetta","Leigha","Evie","Lael","Shelia","Clora","Otelia","Rosetta"]
#Generates a random integer.
    x = randint(0, len(word_list)-1)
    print (word_list[x])
dessert = input("Give her a dessert? Y/N ")
if dessert == "N":
    print ("She will starve :(")
elif dessert == "Y":
    dessert_list = ["cake","cupcake","Apple Pie", "Chocolate", "Dulce de Leche","Rocky Road Dessert", "Ice Cream"]
    y = randint(0,len(dessert_list)-1)
    print (dessert_list[y])
