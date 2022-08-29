import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass, field 
import csv
from collections import namedtuple

# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------

@dataclass
class Holiday:
    name: str
    date: str 

# String output # Holiday output when printed.
#define a string for printing (human reading) information about a specific holiday
def __str__(self):
    return f"""{name} ({date})"""

           
# -------------------------------------------
# The HolidayList class acts as a wrapper and container
# For the list of holidays
# Each method has pseudo-code instructions
# --------------------------------------------

@dataclass
class HolidayList:
    inner_holidays = []

 #=============================ADD===========================   
    #def __init__(self): #pretty sure i can get rid of this 
    #this looks pretty solid for set up. i will need to work out some magic of adding entries to the modify_holidays  
def validate(date):
    # initializing format
    format = "%Y-%m-%d"
    # checking if format matches the date
    res = True
    try:
        res = bool(datetime.datetime.strptime(date, format))
        return(res)
    except ValueError:
        res = False
        return(res)


def add_a_holiday(modify_holidays):
    print('\nAdd a Holiday\n================\nPlease enter the name of the holiday you would like to add.')
    entry = True
    while True:
        add_holiday = input('\nHoliday Name: ')
        add_date = input('\nHoliday Date (in YYYY-MM-DD format): ')
        date = add_date 
        if  validate(date) == True:
                pass
        elif validate(date) == False:
            print('Error:\nInvalid date. Please enter date in correct YYYY-MM-DD format.')
            continue
            #new_holiday_date = add_date
            #holiday_obj.append(new_holiday_date)
         
        #confirm
        if not any(n['Name'] == add_holiday for n in modify_holidays):
            print("Don't see any holidays with that name!")
        elif not any(d['Date'] == add_date for d in modify_holidays):
            print("Don't see any holidays with date!")
        else:
            print('That holiday is already in the Holiday Manager.')
            Choice = input('\nWould you like to try a different holiday [y/n]?: ')
            if choice == 'y':
                add_a_holiday(modify_holidays)
            elif choice == 'n':
                main(modify_holidays)
            else:
                print('Invalid response. Please answer y or n.')
        
        confirm = input("\nConfirm you would like to add {}" .format(add_holiday) + " on {}" .format(add_date) + ". [y/n]: ")
        #if confirmed
        if confirm == 'y':
            # print to the user that you added a holiday 
            print("Success:\n{}" .format(add_holiday) +  " ({}) has been added to the holiday list.".format(add_date))
            #do some magic to add it to the list
            holiday_obj = {"name": add_holiday, "date": add_date} #i may not need quotes on my keys i think this is correct https://www.geeksforgeeks.org/appending-a-dictionary-to-a-list-in-python/ 
            # Use modify_holidays.append(holiday_obj) to add holiday
            modify_holidays.append(holiday_obj) 
            print("Be sure to save your changes before exiting Holiday Manager!")

            #do you want to do it again?
            choice = input('\nWould you like to add a different holiday? [y/n]: ')
            if choice == 'y':
                add_a_holiday(modify_holidays)
            elif choice == 'n':
                main(modify_holidays)
            else:
                print('Invalid response. Please answer y or n.')
        #if NOT confirmed
        elif confirm == 'n':
            print("\n{} has NOT been added to the holiday list.".format(add_holiday))
            #do you want to do it again?
            choice = input('\nWould you like to add a different holiday? [y/n]: ')
            if choice == 'y':
                add_a_holiday(modify_holidays)
            elif choice == 'n':
                main(modify_holidays)
            else:
                print('Invalid response. Please answer y or n.')
        else:
            print('Invalid response. Please answer y or n.')



        # Make sure holiday_obj is an Holiday Object by checking the type

            

    # def findHoliday(HolidayName, Date):
    #     print('Find a Holiday\n================\n)
    #     # Find Holiday in modify_holidays
    #     # Return Holiday


#=============================REMOVE===========================
def remove_a_holiday(modify_holidays):
    print('Remove a Holiday\n================\nPlease enter the name of the holiday you would like to remove.')
    remove_holiday = input('\nHoliday Name: ')
    remove_date = input('\nHoliday Date (YYYY-MM-DD): ')
    date = remove_date 
    entry = True
    while entry == True:
        try:
            entry = bool(datetime.datetime.strptime(date, "%Y-%m-%d"))
        except ValueError:
            print('Error:\nInvalid date. Please enter date in correct YYYY-MM-DD format.')
            remove_a_holiday(modify_holidays)
             
        # Find Holiday in modify_holidays by searching the name and date.
        mod = [elem for elem in modify_holidays if (elem.get('Name')!= remove_holiday or elem.get('Date')!=remove_date)]
        
        if mod == modify_holidays:
            print("Sorry, we dont have {}" .format(remove_holiday) + " on {}" .format(remove_date) + ".")
            choice = input('\nWould you like to try a different holiday [y/n]?: ')
            #remove = True
            #while remove == True:
            if choice == 'y':
                #remove == False
                remove_a_holiday(modify_holidays)
                break
            elif choice == 'n':
                #remove == False
                main(modify_holidays)
                break 
            else:
                print('Invalid response. Please answer y or n.')
                
        else:
            print("Found {}" .format(remove_holiday) + " on {}" .format(remove_date) + ".")
            confirm = input("\nConfirm you would like to remove {}" .format(remove_holiday) + " on {}" .format(remove_date) + ". [y/n]: ")
                #if confirmed
            if confirm == 'y':
                # remove the Holiday from modify_holidays
                modify_holidays = mod
                # inform user you deleted the holiday
                print("Success:\n{} has been removed from the holiday list.".format(remove_holiday))
                #do you want to do it again?
                choice = input('\nWould you like to remove a different holiday? [y/n]: ')
                if choice == 'y':
                    remove_a_holiday(modify_holidays)
                elif choice == 'n':
                    main(modify_holidays)
                else:
                    print('Invalid response. Please answer y or n.')
            #if NOT confirmed
            elif confirm == 'n':
                print("\n{} has NOT been removed from the holiday list.".format(remove_holiday))
                #do you want to do it again?
                choice = input('\nWould you like to remove a different holiday? [y/n]: ')
                if choice == 'y':
                    remove_a_holiday(modify_holidays)
                elif choice == 'n':
                    main()
                else:
                    print('Invalid response. Please answer y or n.')
            else:
                print('Invalid response. Please answer y or n.')

            
        

#=============================READ===========================
def read_json():
    inner_holidays = []
    # Read in things from json file location
    # Use add_a_holiday function to add holidays to inner list.
    with open("holidays.json") as holijson:
        holidays = json.load(holijson)
        inner_holidays.append(holidays)
        modify_holidays = inner_holidays
        return
        

#=============================SAVE===========================
def save_to_json(modify_holidays):
    # Write out json file to selected file.
    choice = input("Would you like to save? [y/n]: ")
    if choice == 'y': 
        with open("holidays.json", "w") as f:
            json.dump(modify_holidays, f, ensure_ascii = False) 
            print('Your progress has been saved.')
            main(modify_holidays)
    elif choice == 'n':
        main(modify_holidays)
    else:
        print('Invalid response. Please answer y or n.')


#=============================SCRAPE AND DISPLAY ===========================        
def scrapeHolidays():
    for i in range(2020,2024+1):
        url = f'https://www.timeanddate.com/holidays/us/{i}'
        soup = BeautifulSoup(requests.get(url).text, 'html')

        out = [[td.text.strip() for td in tr.select('th, td')] for tr in soup.select('tr[data-mask]')]

        with open('1file.csv', 'a') as f_out:
            writer=csv.writer(f_out)
            writer.writerows(out)
        # Scrape Holidays from https://www.timeanddate.com/holidays/us/ 
        # Remember, 2 previous years, current year, and 2  years into the future. 
        # You can scrape multiple years by adding year to the timeanddate URL. 
        # For example https://www.timeanddate.com/holidays/us/2022
        # Check to see if name and date of holiday is in inner_holidays array
        # Add non-duplicates to inner_holidays
        # Handle any exceptions.     

#=============================COUNT HOLIDAYS ===========================   
def numHolidays(modify_holidays):
    modify_holidays = {"holidays": 'holidays'}
    # len(holiday_list)#? not sure is this is the right thing to check the length of
    # Return the total number of holidays in modify_holidays
    print("\nWe currently have  holidays listed!\n")

    #=============================VIEW HOLIDAYS=========================== 
def view_holidays(modify_holidays):
    print("\nView Holidays\n=================\n")
    year = input("Which year?: ")
    week = input("Which week? [1-52, Leave blank for the current week]: ")

    # def filter_holidays_by_week(year, week_number):
    #     Use a Lambda function to filter by week number and save this as holidays, use the filter on modify_holidays
    #     Week number is part of the the Datetime object
    #     Cast filter results as list
    #     return your holidays

    # def displayHolidaysInWeek(holidayList):
    #     Use your filter_holidays_by_week to get list of holidays within a week as a parameter
    #     Output formated holidays in the week. 
    #     * Remember to use the holiday __str__ method.

    # def getWeather(weekNum):
    #     Convert weekNum to range between two days
    #     Use Try / Except to catch problems
    #     Query API for weather in that week range
    #     Format weather information and return weather string.

    # def viewCurrentWeek():
    #     Use the Datetime Module to look up current week and year
    #     Use your filter_holidays_by_week function to get the list of holidays 
    #     for the current week/year
    #     Use your displayHolidaysInWeek function to display the holidays in the week
    #     Ask user if they want to get the weather
    #     If yes, use your getWeather function and display results

#=============================EXIT===========================
def exit(modify_holidays, inner_holidays):
    exit_now = True
    list_1 = inner_holidays
    list_2 = modify_holidays

    while exit_now == True:
        for i in list_1:
            if i not in list_2:
                print('Exit\n=====\n')
                choice = input('\nAre you sure you want to exit?\nYour changes will be lost. [y/n]')
                if choice == 'y':
                    print('Goodbye!')
                    quit()
                elif choice == 'n':
                    main()
                else:
                    print('Invalid response. Please answer y or n.')
            else:
                print('Exit\n=====\n')
                choice = input('\nAre you sure you want to exit?\n[y/n]')
                if choice == 'y':
                    print('Goodbye!')
                    quit()
                elif choice == 'n':
                    main()
                else:
                    print('Invalid response. Please answer y or n.')


def main(modify_holidays):
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    inner_holidays = []
    read_json()    
    modify_holidays = inner_holidays
    # 2. Load JSON file via HolidayList read_json function
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
    # 3. Create while loop for user to keep adding or working with the Calender
    numHolidays(modify_holidays)
    # 4. Display User Menu (Print the menu)
    # Creating a multiline string
    menu_str = "Holiday Menu\n================\n1. Add a Holiday\n2. Remove a Holiday\n3. Save Holiday List\n4. View Holidays\n5. Exit\n"
    print(menu_str)

    # 5. Take user input for their action based on Menu and check the user input for errors
    at_main = True
    while at_main:
        choice = input('\nTo which number option would you like to go? [1/2/3/4/5]: ')        
        if(choice.strip() == "1"):
            at_main = add_a_holiday(modify_holidays)
        elif(choice.strip() == "2"):
            at_main = remove_a_holiday(modify_holidays)
        elif(choice.strip() == "3"):
            at_main = save_to_json(modify_holidays)
        elif(choice.strip() == "4"):
            at_main = view_holidays(modify_holidays)
        elif(choice.strip() == "5"):
            at_main = exit(modify_holidays, inner_holidays)
        else:
            print("\nThat is not a choice. You need to enter 1, 2, 3, 4, or 5.\n")   
    # 6. Run appropriate method from the HolidayList object depending on what the user input is
    # 7. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 
def start():
    modify_holidays = []
    print("\nWelcome the the Holiday Manager!")
    main(modify_holidays)

if __name__ == "__main__":
    start()


# Additional Hints:
# ---------------------------------------------
# You may need additional helper functions both in and out of the classes, add functions as you need to.
#
# No one function should be more then 50 lines of code, if you need more then 50 lines of code
# excluding comments, break the function into multiple functions.
#
# You can store your raw menu text, and other blocks of texts as raw text files 
# and use placeholder values with the format option.
# Example:
# In the file test.txt is "My name is {fname}, I'm {age}"
# Then you later can read the file into a string "filetxt"
# and substitute the placeholders 
# for example: filetxt.format(fname = "John", age = 36)
# This will make your code far more readable, by seperating text from code.





