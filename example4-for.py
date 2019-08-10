import random

sameDay = 0
totalSims = 100000

for i in range(totalSims):
    firstPersonDay = random.randint(1,365)
    secondPersonDay = random.randint(1,365)
    if (firstPersonDay == secondPersonDay) is True:
        sameDay += 1
        
print("Chance of two people being born on the same day: " + str(sameDay*100/totalSims) + "%")

#What edge case am I missing?