num = 600851475143
biggest = 0


for i in range(2, num):
    if (num % i) == 0:
        biggest = i

print(biggest)