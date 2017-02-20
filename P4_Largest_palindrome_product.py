#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.


maxNum = 1

myList = []

def checkPalindrome(product):
    temp = product
    while temp > 1:
        myList.append(temp % 10)
        temp = temp / 10
        
    length = len(str(product))
    if(length == 5):
        if(myList[0] == myList[4] and myList[1] == myList[3]):
            return True
    else:
        if(myList[0] == myList[5] and myList[1] == myList[4] and myList[2] == myList[3]):
            return True
        
    return False


for i in range(101, 1000, 1):
    for j in range(101, 1000, 1):
        product = i * j
        ans  = checkPalindrome(product)
        if(ans == True and product > maxNum):
            maxNum = product

print(maxNum)

