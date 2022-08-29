# 07-assessment
Holiday Manager Project


Unit 07: Object Oriented Data Modeling

Overview
When studying object-oriented programming, a common phrase is "everything is an object." In this module, we looked at object-oriented programming concepts in Python and whether the phrase "everything is an object" holds. First, we explored Python at a basic level - with variables, loops, conditionals, and functions. We built on that foundation with lambdas, magic methods, and classes. Once the foundation solidified, we were introduced to a couple of commonly used tasks in a web-based environment - web scraping and working with APIs.

Assessment Project
This Holiday Manager Project is an example of my object oriented data modeling.

THe High-Level Requirements for this project are:
- The application user is a member of the marketing team.
- The admin needs to be able to manage holidays in an easy-to-use interface.
- The admin already knows about a starting JSON file named holidays.json and appreciates that we have seeded the application with a base of holidays.
- They want all of the holidays from https://www.timeanddate.com/holidays/us/ to also be preloaded.
**NOTE: Only preload holidays with concrete dates. Do not calculate holiday dates. The team expects you to include holidays from the present year, 2 years of past holidays, and 2 years of future holidays.


- The holidays must be saved in JSON, following the formatting of the provided file.
- With the holidays approaching, the marketing person may want to know what the weather looks like so they can determine what to market more. Use a weather API to show what the weather looks like for the current period. (See the notes below for details.) We recommend Open Weather Map API, but you are free to use any weather API you would like.

How to use the Holiday Manager
The main file for this project is 'Holiday_Manager_Vanessa_Gleason.py'. This is where most of the activity takes place. 

Inside the Holiday Manager are five main sections:
1. Adding a Holiday - where a user can add a holiday to the holiday list
2. Remove a Holiday - where the user can remove a holiday currently on the holiday list
3. Save - where any progress made in the user session can be saved
4. View Holidays - where a user can specify a specific year and a specific week in that year to see what the holidays are. A bonus featuer of this section is if the current week is selected, (by not entering any week number) the weather for that week is also displayed.
5. Exit - this is section to go to if you are done in the Holiday Manager. IF there is unsaved progress, it was prompt you to confirm you do not want to save your progress.

There are additional files: 
- config.py which is in my gitignore, that has the API key to the weatehr API
- holidays.json - this is the file that is read into the Holiday Manager and is also the file to which any changes to the Holiday Manager list of holidays is saved.
- Plans folder, which has my brainstoming documentation 

Please enjoy my Holiday Manager. I'm just starting out in data but excited to see where I go!
Thanks,
Vanessa



