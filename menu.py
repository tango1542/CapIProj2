import os
from create import create_database
from insert import insert_database
from update import update_database
from delete import delete_database
from displayAll import displayAll_database
from inputDisplay import inputDisplay_database



def print_menu():  ## Your menu design here
    print ("\nPlease Select a menu option\n")
    print ("1. Create a database and table")
    print ("2. Add a row of data to the database table")
    print ("3. Update a row in the database table")
    print ("4. Delete a row in the database table")
    print ("5. Display all the rows in the database table")
    print("6. Display a single row of data based on the input value")
    print (67 * "-")


loop = True

while loop:  ## While loop which will keep going until loop = False
    print_menu()  ## Displays menu
    choice = int(input("Enter your choice [1-6]: "))

    if choice == 1:
        create_database()
        # print ("Menu 1 has been selected")
        # os.system('create.py')
        ## You can add your code or functions here
    elif choice == 2:
        insert_database()
        ## You can add your code or functions here
    elif choice == 3:
        update_database()
        ## You can add your code or functions here
    elif choice == 4:
        delete_database()
        ## You can add your code or functions here
    elif choice == 5:
        displayAll_database()
        ## You can add your code or functions here

    elif choice == 6:
        inputDisplay_database()
        ## You can add your code or functions here
        loop = False  # This will make the while loop to end as not value of loop is set to False

    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection. Enter any key to try again..")
