def main():
    #Problem1()
        Problem2()
#Problem 1:
#We will keep having this problem until EVERYONE gets it right without help
#Create a function that has a loop that quits with q.
# If the user doesn't enter q, ask them to input another string.
#BONUS: Make sure the code can handle whatever case the User enters
# the q as (uppercase or lowercase)

def Problem1():
    while (True):
        userInput = input("Enter a q to quit")
        if userInput =='q':
            print("correct")
            break

#Write 2 functions: exercise2() and exercise2_helper(num1, num2, num3. operation)
#The function exercise2_helper(num1, num2, num3) should expect 3 numbers,
# and an operation to perform as a String as parameters.
#The function should support 3 operations:
#SUM - Return the sum of the 3 numbers
#PROD - Return the product of the 3 numbers
#AVG - Return the average of the 3 numbers
#The operation and the returned value should then be printed out
# back in the main exercise2() function. Return INVALID OPERATION if an
# operation passed in that isn't supported. HINT: Use switch/case

def Problem2():
    exercise2()





def exercise2():
    exercise2_helper()

def exercise2_helper(num1, num2, num3):
    userInput1 = input(int("Enter a number"))
    userInput2 = input(int("Enter a number"))
    userInput3 = input(int("Enter a number"))
    addTheNums = (userInput1 + userInput2 + userInput3)
    getTheProd = (userInput1*userInput2*userInput3)
    getTheAvg = (addTheNums/3)













if __name__ == '__main__':
    main()
