from datetime import datetime
import json
from bs4 import BeautifulSoup
import requests
from dataclasses import dataclass


# -------------------------------------------
# Modify the holiday class to 
# 1. Only accept Datetime objects for date.
# 2. You may need to add additional functions
# 3. You may drop the init if you are using @dataclasses
# --------------------------------------------
#re-read data classes lesson
class Holiday:
 
   
    # Initializer: user gives ingredients, this is the recipe to make the cookie
    #break it out of the @dataclass so I can see what is going on
    def __init__(self, holiday_name, date_str, date_format='%Y-%m-%d'):
        self._name = holiday_name
        self._date = datetime.strptime(date_str, date_format)    #make sure it is in correct date format and put it in datetime
    
    # String format: cookie, what is your name?
    def __str__ (self):
        return self._name #self so the cookie looks at itself and says its name
    
    # Then the getters

    # Name getter
    @property
    def name(self):
        return self._name
    
    # Date getter
    @property
    def date(self):
        return self._date
    
    # THen the setters

    # Name setter
    @name.setter
    def name(self, new_name):
        self._name = new_name #setting the new name 
    
    # Date setter
    @date.setter
    def date(self, new_date_str, date_format):
        self._date = datetime.strptime(new_date_str, date_format) #as datetime, NOT string 
        #that makes one instance of a cookie
# -------------------------------------------
# The HolidayList class acts as a wrapper and container - "the cookie jar"
# For the list of holidays - the "cookies"
# Each method has pseudo-code instructions
# --------------------------------------------

# the cookie jar maker - Tom and I could like different cookies in our jars. There is NOT a community cookie jar
class HolidayList:
    #all the steps stay in the holidayList class
    #all going to have to reference 'self'
    def __init__(self):
        self._inner_holidays = []

    #gunna need to get the holidays
    # inner_holidays getter
    @property
    def inner_holidays(self):
        return self._inner_holidays
    


    # so, really, it might make more sense to have the machinery to to make the cookie in these 
    # definitions and the user input - providing ingredients in the main category
    def add_a_holiday(self, holiday_obj): #steps to add a holiday(cookie) (from the Class Holiday recipe) to HolidayList (cookie jar)
                # Make sure the holiday_obj is a holiday object by checking the type
        if (type(holiday_obj) == Holiday):
            
                # Use innerHolidays.append(holiday_obj) to add holiday
                self._inner_holidays.append(holiday_obj)

        # If not holiday instance
        else:
            raise Exception("Input object must be Holiday type!")
        


    def findHoliday(self, holiday_name, date):
        date_format='%Y-%m-%d'

        # Find Holiday in innerHolidays
        date = datetime.strptime(date, date_format)
        for holiday in self._inner_holidays:
            if (holiday.name == holiday_name and holiday.date == date):
                # Return Holiday
                return holiday
        
        # Return none if no holiday found
        return None


    def remove_a_holiday(self, holiday_name, date):
        # Find Holiday in innerHolidays by searching the name and date combination.
        date_format= '%Y-%m-%d'
        date = datetime.strptime(date, date_format)
        so_long_cookie = False
        while so_long_cookie == False:
            for i in range(len(self._inner_holidays)):
                holiday = self._inner_holidays[i]
 
                if (holiday.name == holiday_name and holiday.date == date):
                    so_long_cookie = True

                    # Delete object
                    self._inner_holidays.pop(i)
                    return

            # Return none if no holiday found
            so_long_cookie = True
            print(f'Holiday ("{holiday_name}", "{date}") could not be found, so no holiday has been deleted!')



    def read_json(self):
        
        # Read in things from json file location
        with open('holidays.json', 'r') as f:
            data = json.load(f)['holidays']

            # Iterate through each JSON obj and create a new holiday
            for holiday_json in data:
                holiday = Holiday(holiday_json['name'], holiday_json['date'])

                 # Use add_a_holiday function to add holidays to inner list.
                self.add_a_holiday(holiday)

       

    def save_to_json(self, save_name):

        # Write out json file to selected file.
        date_format='%Y-%m-%d'
        # Convert data into dictionary format
        cookie_jar = []
        for holiday in self._inner_holidays:
            cookie = dict()
            cookie['name'] = holiday.name
            cookie['date'] = holiday.date.strftime(date_format)
            cookie_jar.append(cookie)

        # Write file # https://stackoverflow.com/questions/25778021/how-can-i-save-a-list-of-dictionaries-to-a-file
        with open(save_name, 'w') as f:
            for cookie in cookie_jar:
                json.dump(cookie, f)
                f.write("\n")
        
    # # def scrapeHolidays(self): TODO
    #     for year in range(int(datetime.today().year)-2, int(datetime.today().year)+3):
    #         url = f'https://www.timeanddate.com/holidays/us/{year}'
    #         soup = BeautifulSoup(requests.get(url).text, 'html')

    #     out = [[td.text.strip() for td in tr.select('th, td')] for tr in soup.select('tr[data-mask]')]

    #     with open('file.csv', 'a') as f_out:
    #         writer=csv.writer(f_out)
    #         writer.writerows(out)
    #         #scrape the holiday
    #         # check if holiday is on list
    #         # Add holiday to list
    #         # Print success message
    #     print(f'"{holiday}" ({date}) has been added!')
 

    def numHolidays(self):
        # Return the total number of holidays in innerHolidays
        num = len(self._inner_holidays)
        print("\nWe currently have {} holidays listed!\n" .format(num))
        return


    #   year: (int) year of the holidays
    #   week_number: (int) week number (range is 1 to 52, inclusive)
    #   return: (list(Holiday)) holidays within that timeframe
    def filterHolidaysByWeek(self, year, week_number): #1) get the holidays of a specific week in a specific year

        # save as holidays # Get only dates with week number
        holidays = list(filter(lambda holiday: int(holiday.date.isocalendar()[1]) == week_number # date.isocalendar()[1] = week NUM https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
            and int(holiday.date.isocalendar()[0]) == year, self._inner_holidays)) # date.isocalendar()[0] = year

        # return your holidays
        return holidays #goes to def displayHolidaysInWeek
        
  

        # Use your filterHolidaysByWeek to get list of holidays within a week 
    def displayHolidaysInWeek(self, holidays):

        # Output formatted holidays in the week. 
        format_holidays = []

        # Format strings
        for holiday in holidays:
            date = str(holiday.date)
            format_holidays.append(f'{holiday.name} ({holiday.date.date()})') #https://stackoverflow.com/questions/26153795/display-python-datetime-without-time

        # Return list of formatted holidays
        return format_holidays


    # def getWeather(weekNum): ...lets not push it
        # Convert weekNum to range between two days
        # Use Try / Except to catch problems
        # Query API for weather in that week range
        # Format weather information and return weather string.

    def viewCurrentWeek(self): 

        # Use the Datetime Module to look up current week and year
        year = datetime.now().year
        week = datetime.now().isocalendar()[1]

        # Use your filterHolidaysByWeek function to get the list of holidays 
        holidays = self.filterHolidaysByWeek(year, week)

        # Use your displayHolidaysInWeek function to display the holidays in the week
        self.displayHolidaysInWeek(holidays)


def main():
    # Large Pseudo Code steps
    # -------------------------------------
    # 1. Initialize HolidayList Object
    holidays = HolidayList()
    #probably stick the welcome from start here?
    print("\nWelcome the the Holiday Manager!")
    
    # 2. Load JSON file via HolidayList read_json function
    holidays.read_json()
    
    # 3. Scrape additional holidays using your HolidayList scrapeHolidays function.
        #holidays.scrapeHolidays() 
    #Probably stick the counter here too.
    holidays.numHolidays()
    # 4. Create while loop for user to keep adding or working with the Calender
    makin_cookies = True #are we still making/looking at/removing cookies? ok, keep going 
    saved = True
    while (makin_cookies): #now everything is going to have to indent...this is maybe better to have
        #the UI here for flow...
    # 5. Display User Menu (Print the menu)
        
        menu_str = "\nHoliday Menu\n================\n1. Add a Holiday\n2. Remove a Holiday\n3. Save Holiday List\n4. View Holidays\n5. Exit\n"
        print(menu_str)

    # 6. Take user input for their action based on Menu and check the user input for errors

        choice = input('\nTo which number option would you like to go? [1/2/3/4/5]: ')        
        # 7. Run appropriate method from the HolidayList object depending on what the user input is
  
        #move add a holiday UI (ingredient acceptance) here:
        if(choice.strip() == "1"):
            #keep indented
            #header and instructions
            print('\nAdd a Holiday\n================\nPlease enter the name of the holiday you would like to add.')
            #get the ingredients to make a holiday cookie

            #1) name of holiday                      
            holiday_name = input('\nHoliday Name: ') 

            #2) date of holiday - while loop it to see if it is valid
            quality_ingedient = False
            while quality_ingedient == False:
                date = input('\nHoliday Date (in YYYY-MM-DD format): ')
            #bring/modify validate date function here
                try:
                    datetime.strptime(date, '%Y-%m-%d')
                    quality_ingedient = True
                except:
                    print('Error:\nInvalid date. Please enter date in correct YYYY-MM-DD format.')
            
            #does this cookie exist?
            #rework once I got my find working            
            exists = holidays.findHoliday(holiday_name, date)
            if (exists == None):# New cookie!!
                holiday_obj = Holiday(holiday_name, date)
                holidays.add_a_holiday(holiday_obj) #the cookie creator!!
                print("\nSuccess:\n{}" .format(holiday_name) +  " ({}) has been added to the holiday list.".format(date))
                print("\nBe sure to save your changes before exiting Holiday Manager!\n")
                saved = False

            else:# Existing cookie...
                print('That holiday is already in the Holiday Manager.\n')
          
            # Return to main menu
            print('What would you like to do next?\n')

        #move remove holiday UI (ingredient acceptance) here:
        elif(choice.strip() == "2"):
            #Header and instructions
            #keep indented
            print('\nRemove a Holiday\n================\nPlease enter the name of the holiday you would like to remove.')
            #1) name of holiday
            holiday_name = input('\nHoliday Name: ')

            #2) date of holiday - copied from add date
            quality_ingedient = False
            while quality_ingedient == False:
                date = input('\nHoliday Date (in YYYY-MM-DD format): ')
                
                try:
                    datetime.strptime(date, '%Y-%m-%d')
                    quality_ingedient = True
                except:
                    print('Error:\nInvalid date. Please enter date in correct YYYY-MM-DD format.')
            
            #does this cookie exist? copied/modified from add date           
            exists = holidays.findHoliday(holiday_name, date)
            if (exists != None):# Get rid of the cookie!!

                holidays.remove_a_holiday(holiday_name, date) #the cookie destroyer!!
                print("\nSuccess:\n{}" .format(holiday_name) +  " ({}) has been removed from the holiday list.".format(date))
                print("\nBe sure to save your changes before exiting Holiday Manager!\n")
                saved = False

            else:# non-existent cookie...
                print('That holiday is not in the Holiday Manager.\n')
          
            # Return to main menu
            print('What would you like to do next?\n')
        
        
        #move save UI (ingredient acceptance) here:
        elif(choice.strip() == "3"):
             # Display page info
            print("\nSaving Holiday List\n====================\n")

            # Get response
            quality_ingedient = False
            while (not quality_ingedient):
                choice = input("Would you like to save your Holiday List? [y/n]: ")

                # Save data
                if (choice == 'y'): # Save data

                    # we are NOT saving a community file. Tom's is different than mine
                    qualitier_ingedient = False
                    while (not qualitier_ingedient):
                        name = input("Please input what you would like to call your file: ")
                        if (".json" in name):
                            print("Please do not include '.json' in input!")
                        else:
                            qualitier_ingedient = True
                            save_name = ('{}'.format(name)+'.json')
                    
                    # Save file
                    holidays.save_to_json(save_name)
                    saved = True
                    
                    # Print success message
                    print()
                    print("Success:\nYour changes have been saved to {}".format(save_name))

                    # Return to main menu
                    print('\nWhat would you like to do next?\n')
                    quality_ingedient = True

                # Don't do any thing
                elif (choice == 'n'):
                    
                    # Print message
                    print()
                    print("\nCanceled: \nHoliday list has NOT been saved.\n")

                    # Return to main menu
                    print('\nWhat would you like to do next?\n')
                    quality_ingedient = True
                
                # Bad input
                else:
                    print("Please enter 'y' or 'n'!")
            
        
        #move view holiday UI (ingredient acceptance) here:
        elif(choice.strip() == "4"):
            #header/info
            print("\nView Holidays\n=============\n")
            # year = input("Which year?: ")
            # week = input("Which week? [1-52, Leave blank for the current week]: ")
 
             # Get year range
            year_min = None
            year_max = None
            for holiday in holidays.inner_holidays:
                if (year_min == None or year_min > holiday.date.year):
                    year_min = holiday.date.year
                if (year_max == None or year_max < holiday.date.year):
                    year_max = holiday.date.year
            
            # Get year and month
            which_year = int(input("Which year?: ")) #https://www.geeksforgeeks.org/how-to-take-integer-input-in-python/
            which_week = int(input(f'Which week (current week: {datetime.today().isocalendar()[1]})? [1-52]: ')) #https://www.programiz.com/python-programming/datetime/current-datetime
            
            if which_week == '':
                which_week == datetime.today().isocalendar()[1]

            # Display results
            print()
            print(f'These are the holidays for {which_year} week #{which_week}:')
            print('==================================================')
            what_you_want=holidays.displayHolidaysInWeek(holidays.filterHolidaysByWeek(which_year, which_week))
            print(*what_you_want, sep = "\n") #https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
            print('\nWhat would you like to do next?\n')
          
          
        
        #move exit holiday UI (ingredient acceptance) here:
        elif(choice.strip() == "5"):
            #header/info
            print('\nExit\n=====\n')
            if saved == False : # Only display if changes have been made that haven't been saved
                print("Your unsaved changes will be lost!")
             # Get response
            is_this_goodbye = False
            while is_this_goodbye == False:           
                choice = input('\nAre you sure you want to exit?\n[y/n]: ')
                if choice == 'y':
                    print('Goodbye!')
                    makin_cookies = False
                    is_this_goodbye = True
                elif choice == 'n':
                    print('\nWhat would you like to do next?\n')
                else:
                    print('Invalid response. Please answer y or n.')

        #if user did not put in 1-5
        else:
            print("\nThat is not a choice. You need to enter 1, 2, 3, 4, or 5.\n")   

    # 8. Ask the User if they would like to Continue, if not, end the while loop, ending the program.  If they do wish to continue, keep the program going. 


if __name__ == "__main__":
    main()


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





