"""7.Birth Year
The program prompts the user their birth year. Assuming a person’s age
is a non-negative integer not exceeding 120, output the user’s age or the
words “Incorrect Year”. The sample outputs assume it’s currently the year
2016. If you are writing this program during any other year, the correct
answers may differ. Store the value of the current year in a variable.
Sample Input Sample Output
2016      0
2018      Incorrect Year
1903      113
1803      Incorrect Year
1991      25"""

year = int(input('Birth year'))
year_now = 2024
birth = year_now - year

if year > 2024:
    pass
elif year < 1903:
    pass
else:
    print(birth)
    

