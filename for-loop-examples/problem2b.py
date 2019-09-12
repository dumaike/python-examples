#Make a pyramid of hearts of any height. For example, a 4 height pyramid would be:
#   <3
#  <3<3
# <3<3<3
#<3<3<3<3

towerHeight = 4

for i in range(towerHeight):
    for j in range(towerHeight - i):
        print(" ", end='')
        
    for j in range(i + 1):
        print("<3", end='')
    print("")