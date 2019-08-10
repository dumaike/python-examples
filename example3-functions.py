def daysOld(currentMonth, currentDay, currentYear, birthMonth, birthDay, birthYear):
    
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
    
    return totalDaysOld

mikeDaysOld = daysOld(8, 10, 2019, 5, 10, 1984)
mariaDaysOld = daysOld(8, 10, 2019, 12, 7, 1988)

if (mikeDaysOld > mariaDaysOld):
    print("Mike is older than Maria!")
else:
    print("Maria is older than Mike!")