#Take a list of numbers, and return how many of them are even numbers. 
#For example [1, 3, 4, 5, 7, 7, 2, 4, 23, 5] would be 3
#Challenge: Only return unique even numbers, which would be 2 in the above example.

numberList = [1, 3, 4, 5, 7, 7, 2, 4, 23, 5]

count = 0
for i in numberList:
    if i % 2 == 0:
        count = count + 1
        
print(count)