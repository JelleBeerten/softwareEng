#Name:          Jelle Beerten
#Date:          18/09/2018
#Description:   calculates the total sum of all even numbers on the fibonacci streak below 4mil

totalsum = 0
placeholder = 1
secondplaceholder = 0
endsum = 0

while totalsum < 4000000:
        totalsum = placeholder + secondplaceholder
        placeholder = secondplaceholder
        secondplaceholder = totalsum
        if totalsum%2 == 0:
            endsum +=totalsum
print(endsum)



