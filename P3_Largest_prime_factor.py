#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?
#Tutorial:
#http://www.geeksforgeeks.org/print-all-prime-factors-of-a-given-number/
maxPN = 1
i = 2
n = 600851475143

while n % 2 == 0:
    n = n / 2
    maxPN = 2

temp = n

for i in range(3, int(pow(temp, 0.5)) + 1, 2):
    if n % i == 0:
        maxPN = i
        n = n / i
        
print(maxPN)
