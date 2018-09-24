#Name:          Jelle Beerten
#Date:          18/9/2018
#description:   finds the total sum of the numbers 1-1000 wich are devideble by 3 or 5

totalsum = 0
for number in range(1, 1000):
    if (number % 3 == 0) or (number % 5 == 0):
        totalsum += number
print(totalsum)

