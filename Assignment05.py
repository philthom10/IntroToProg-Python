# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# PThompson,5.15.2023,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection
saveStatus = True  # PT: status of if file has been saved since last change to data

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFile = open(objFile, "r")  # PT: opening file in read mode
for row in objFile:  # PT: goes through each line in file
    strData = row.split(",")  # PT: returns a list with two elements, items that were sep by comma file
    dicRow = {"Task":strData[0], "Priority":strData[1].strip()}  # PT: indexes string created by file and keys to dict.
    lstTable.append(dicRow)  #  PT: makes list "table" with dictionary elements as "rows"
objFile.close()
# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("The current data is: \n")  # PT
        for row in lstTable:  # PT
            print(row["Task"] + " | " + row["Priority"])  # PT: calls elements of row by key in dictionary
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strNewTask = input("Task name: ").title().strip()  # PT:  captures user input and uses strip method
        strNewRank = input("Task priority (High, Medium, Low): ").capitalize().strip()  # PT
        lstTable.append({"Task": strNewTask, "Priority": strNewRank})  # PT: appending table with new entries
        saveStatus = False  # PT: Toggles back to false if updated after saving to file
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemoval = input("Which task would you like to delete? ").strip().title()  # PT
        counter = 0  # PT: For counting removals to aid in giving user feedback
        for row in lstTable:
            if row["Task"].lower() == strRemoval.lower():  # PT: searches each row in table for entered value
                lstTable.remove(row)  # PT: removes row from table if it has selected value
                counter += 1
        if counter > 0:  # PT: counter will be over 0 only if a row item was removed
            print("\n  The task '" + strRemoval + "' was removed from the list!")
        elif counter == 0:  #PT: if counter is zero, no removals were made
            print("\n  The task '" + strRemoval + "' was not in the original list. Please select a menu option.")
        saveStatus = False  # PT: toggles back to false if updated after saved
        continue
    # Step 6 - Save tasks to the ToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFile = open("ToDoList.txt", "w")  # PT
        for row in lstTable:
            objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")  # PT: saves each row to file
        objFile.close()
        saveStatus = True  # PT: toggles save status to true once data has been saved to file
        print("Tasks successfully saved to file.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        # PT: This block checks to see if file has been updated without saving before closing
        # if the file has been updated without saving it asks user if they would like to save before closing
        if saveStatus:  # PT: evaluates if true then breaks and exits
            break
        elif not saveStatus:  # PT: evaluates if not saved (false) then prompts for save choice below
            strSavePick = input(" ATTENTION: You have unsaved changes. "  # PT: prompts for saving if unsaved data
                                "Would you like to save before exiting? (Y or N) ").lower().strip()
            if strSavePick == "y":
                objFile = open("ToDoList.txt", "w")
                for row in lstTable:
                    objFile.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")  # PT: saves to file
                saveStatus = True  # PT: toggles save status to true once data has been saved to file
                print("\nChanges successfully saved to file.")
                break  # and Exit the program
            elif strSavePick == "n":
                break
            else:
                print("\n\t*** Invalid choice, what would you like to do next? *** ")  #PT: goes back to menu
input("\n\nPress the enter key to confirm and exit.")  # PT: Exits whole program upon user input
