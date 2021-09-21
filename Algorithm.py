import AlgorithmModules

# Global Variables grabbed from the module file
newContact1 = AlgorithmModules.contact1
newContact1Email = AlgorithmModules.contact1Email
newContact1Number = AlgorithmModules.contact1Num

newContact2 = AlgorithmModules.contact2
newContact2Email = AlgorithmModules.contact2Email
newContact2Number = AlgorithmModules.contact2Num

newContact3 = AlgorithmModules.contact3
newContact3Email = AlgorithmModules.contact3Email
newContact3Number = AlgorithmModules.contact3Num

newContact4 = AlgorithmModules.contact4
newContact4Email = AlgorithmModules.contact4Email
newContact4Number = AlgorithmModules.contact4Num

newContact5 = AlgorithmModules.contact5
newContact5Email = AlgorithmModules.contact5Email
newContact5Number = AlgorithmModules.contact5Num

# Input for the users desired contact

lookup1 = (input("Welcome, who are you looking for today? "))

# Processing the users choice and deciding if it is a valid option or not

if lookup1 == "newContact1":
    # Outputting the name of the chosen contact
    print("Contact Name: ", newContact1)
    # Asking for the user to input the information needed (email or number)
    lookup2 = (input("What info would you like from this contact? "))
    # Proccessing user choice and outputting the information attached
    if lookup2 == "email":
        print(newContact1, "'s email is ", newContact1Email)
    elif lookup2 == "number":
         print(newContact1, "'s number is ", newContact1Number)
    else:
        print ("That is not available.")
else:
    pass

if lookup1 == "newContact2":
     # Outputting the name of the chosen contact
    print("Contact Name: ", newContact2)
    # Asking for the user to input the information needed (email or number)
    lookup2 = (input("What info would you like from this contact? "))
     # Proccessing user choice and outputting the information attached
    if lookup2 == "email":
        print(newContact2, "'s email is ", newContact2Email)
    elif lookup2 == "number":
         print(newContact2, "'s number is ", newContact2Number)
    else:
        print ("That is not available.")
else:
    pass

if lookup1 == "newContact3":
     # Outputting the name of the chosen contact
    print("Contact Name: ", newContact3)
    # Asking for the user to input the information needed (email or number)
    lookup2 = (input("What info would you like from this contact? "))
    # Proccessing user choice and outputting the information attached
    if lookup2 == "email":
        print(newContact3, "'s email is ", newContact3Email)
    elif lookup2 == "number":
         print(newContact3, "'s number is ", newContact3Number)
    else:
        print ("That is not available.")
else:
    pass

if lookup1 == "newContact4":
     # Outputting the name of the chosen contact
    print("Contact Name: ", newContact4)
    # Asking for the user to input the information needed (email or number)
    lookup2 = (input("What info would you like from this contact? "))
    # Proccessing user choice and outputting the information attached
    if lookup2 == "email":
        print(newContact4, "'s email is ", newContact4Email)
    elif lookup2 == "number":
         print(newContact4, "'s number is ", newContact4Number)
    else:
        print ("That is not available.")
else:
    pass

if lookup1 == "newContact5":
     # Outputting the name of the chosen contact
    print("Contact Name: ", newContact5)
    # Asking for the user to input the information needed (email or number)
    lookup2 = (input("What info would you like from this contact? "))
    # Proccessing user choice and outputting the information attached
    if lookup2 == "email":
        print(newContact5, "'s email is ", newContact5Email)
    elif lookup2 == "number":
         print(newContact5, "'s number is ", newContact5Number)
    else:
        print ("That is not available.")
else:
    pass

if lookup1 != ("newContact1" or "newContact2" or "newContact3" or "newContact4" or "newContact5"):
    print("That is not an available contact")
