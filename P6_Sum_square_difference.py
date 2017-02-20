#The sum of the squares of the first ten natural numbers is,
#
#1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is,
#
#(1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumSq = 0
for i in range(1, 101, 1):
    sumSq = sumSq + i
sumSq = sumSq**2

sqSum = 0
for i in range(1, 101, 1):
    sqSum = sqSum + i**2

print(sumSq - sqSum)

