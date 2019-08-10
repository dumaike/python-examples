birthDay = 10
birthMonth = 5
birthYear = 1984

currentDay = 10
currentMonth = 8
currentYear = 2019

totalDaysOld = 0

# Calculate the days passed in years
yearDiff = currentYear - birthYear
if currentMonth <= birthMonth and currentDay < birthDay:
    yearDiff -= 1
totalDaysOld = 365*yearDiff;    

averageDaysInMonth = 30.42
# Calcualte the days passed in months
monthDiff = currentMonth - birthMonth
if currentMonth <= birthMonth:
    monthDiff += 12
totalDaysOld += monthDiff*averageDaysInMonth

# Calcualte the days passed in months
dayDiff = currentDay - birthDay
if currentDay < birthDay:
    dayDiff += averageDaysInMonth
totalDaysOld += dayDiff

print("You are " + str(totalDaysOld) + " days old!")

#This number is a litte bit off, why?