month = input("Enter the month ('January', ..., 'December'):\n") # Gives the name of the month
month = month.capitalize() 
day = input("Enter the start day ('Monday', ..., 'Sunday'):\n") #The day the month starts on
day = day.capitalize()

print(month)
print("Mo Tu We Th Fr Sa Su")

start_position = 0
end_day = 0
one = 1

#determines how many days in the month
if day == "Monday":
    start_position = 0
    print("%2d" % one, end = ' ')
elif day == "Tuesday":
    start_position = 1
    print("%5d" % one, end = ' ')
elif day == "Wednesday":
    start_position = 2
    print("%8d" % one, end = ' ')
elif day == "Thursday":
    start_position = 3
    print("%11d" % one, end = ' ')
elif day == "Friday":
    start_position = 4
    print("%14d" % one, end = ' ')
elif day == "Saturday":
    start_position = 5
    print("%17d" % one, end = ' ')
elif day == "Sunday":
    start_position = 6
    print("%20d" % one, end = ' ')

if month == "September" or month == "April" or month == "June" or month == "November":
    end_day = 30
elif month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
    end_day = 31
elif month == 'February':
    end_day = 28
    
for current_day in range (2, end_day + 1):
    if(start_position + current_day - 1)%7 == 0:
        print()
    print("%2d" % current_day, end = ' ')
    current_day += 1