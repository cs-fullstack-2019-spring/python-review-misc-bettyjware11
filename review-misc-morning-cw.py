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
    # We should be calling the helper functionand pass in the 4 arguments
    # exercise2_helper()

# KEY: This function should accept 3 numbers and the operation to perform
def exercise2_helper(num1, num2, num3):
    userInput1 = input(int("Enter a number"))
    userInput2 = input(int("Enter a number"))
    userInput3 = input(int("Enter a number"))
    addTheNums = (userInput1 + userInput2 + userInput3)
    getTheProd = (userInput1*userInput2*userInput3)
    getTheAvg = (addTheNums/3)

#################################
# KEY: PROBLEM 2 SOLUTION
#################################
def problem2_solution():
    # Helper function can be nested or outside of this function
    def exercise2_helper_solution(num1, num2, num3, operation):
        if (operation.lower() == "sum"):
            return (num1 + num2 + num3)
        elif (operation.lower() == "prod"):
            return (num1 * num2 * num3)
        elif (operation.lower() == "avg"):
            return ((num1 + num2 + num3) / 3)
        else:
            print("ERROR")

    # Some test data
    n1 = 1
    n2 = 20
    n3 = 30

    # Test each operation (note: handles operation in any case)
    print(f"The SUM of the numbers {n1}, {n2}, {n3} is: {exercise2_helper_solution(n1, n2, n3, 'SUM')}")
    print(f"The PRODUCT of the numbers {n1}, {n2}, {n3} is: {exercise2_helper_solution(n1, n2, n3, 'Prod')}")
    print(f"The AVERAGE of the numbers {n1}, {n2}, {n3} is: {exercise2_helper_solution(n1, n2, n3, 'avg')}")













if __name__ == '__main__':
    main()
