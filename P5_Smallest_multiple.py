#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num = int(input("Enter digit till which we want our range"))

startNum = num**2

flag = False

while(flag == False):
    #counter to count if all the numbers are satisfied or not
    cnt = 0
    for i in range(1, num + 1, 1):
        #check is failed so break for loop
        if(startNum % i != 0):
            break;
        cnt = cnt + 1
    #see if we have our number. set flag and end while loop
    if(cnt == num):
        flag = True
    #decided not to place in else part.    
    startNum = startNum + 1

print(startNum - 1)
