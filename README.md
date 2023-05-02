<p align="center">▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
█░▄▀██░▄▄░█░██░▄▄▀█░▄▄▀█░▄▄▀█░▄▄█░▄▄▀█░▄░████░▄▄░
█░█░██░▀▀░█░██░▀▀░█░██░█░██░█░▄▄█░▀▀▄██▀▄█▀▀█░▀▄░
█▄▄███░████▄▄█▄██▄█▄██▄█▄██▄█▄▄▄█▄█▄▄█░▀▀█▄▄█░▀▀░
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀</p>

### Sample command: python3 generate.py
#### REMINDER: The individual who did duty on the last day of the previous month is unavailable on the first day of the current month. Add this into the input CSV file.

## Background:
This program was created to automate the process of creating a duty list, under the assumption that ONE person must be schedued for each day.  

Version 2.0 features a different algorithm from [V1.0](https://github.com/duckyfuz/dPlanner).  
Mainly to fix the issue of edge cases that completely halt the program.  
Also to clean up the code.

Doing duty rewards one with points, and the amount of points awarded depends on the type of day it is.

### Points System:
Monday - Thurday: 1 point  
Friday: 1.5 points  
Saturday, Sunday: 2 points

### Features: 
~(1) Extras - Punishments carried out on Saturday / Sunday. Clearing an extra means forfeiting the 2 points that usually come with doing duty on the day.~  
~(2) Extras-to-be-done - Individuals do not have to clear all their extras in one month. Each person can indicate how many extras they want to clear in a single month.~  
(3) Points History - Points awarded from previous months are taken into account when planning.   
(4) Points Equity - The variance of all the points will be kept to a minumum.  
(5) Availability - Duty schedue will be planned around each person's availability. 

## Pending Issues:

1. Extras cannot be cleared on a public holiday. 
2. Public holidays do not award one with 2 points. 