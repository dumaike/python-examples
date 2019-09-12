#Find all the numbers between 100 and 1400 where each digit is a 0 or a 1.
#Challenge: Find all the numbers between 100 and 1400 where each digit is non-repeating.

startNumber = 100
endNumber = 1400

for i in range(startNumber, endNumber):
    reducedNumber = i
    valid = True
    while reducedNumber > 0:
        digit = reducedNumber % 10
        reducedNumber = int(reducedNumber / 10)
        if digit > 1:
            valid = False
            break
    if valid:
        print(i)
    