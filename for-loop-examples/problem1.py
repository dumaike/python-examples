#Find all numbers between 1200 and 3200 that are divisible by 5 but not by 7.

startNumber = 1200
endNumber = 3200

count = 0
for i in range(startNumber, endNumber):
    if i % 7 == 0 and i % 5 != 0:
        count = count + 1
        
print(count)