#Program to create a function to check if given number is odd or even
def check(number):
    if(number==0):
        print("The number is zero")
    elif(number%2==0):
        print("The number is even")
    elif(number%2==1):
        print("The number is odd")
    else:
        print("Invalid")
n=int(input("Enter a number: "))
check(n)

