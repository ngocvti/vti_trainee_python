# The Collatz Sequence

def collatz(number):
    if number % 2 == 0:
        even = number // 2
        return even
    else:
        odd = 3 * number + 1
        return odd
       
inputNum = int(input("Enter Number: "))
num = collatz(inputNum)
while num != 1:
    print(num)
    num = collatz(num)
print(num)
    
# Input Validation
VALIDATE = True
while VALIDATE:
    try:
        num = int(input("Press an integer number: "))
        print(f'Yes, your lucky number is {num}')
        VALIDATE = False
    except:
        print("Try again, you'd type an integer number!!!")



    