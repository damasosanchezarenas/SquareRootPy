def exhaustiveEnumeration(goal):
    result=0
    while result**2 < goal:
        result+=1

    if result**2 == goal :
        print(f"The square root of {goal} is {result}")
    else :
        print("The exact square root of this number does not exist")


##exhaustiveEnumeration(goal)

def solutionsApproach(goal):
    epsilon=0.01
    step=epsilon**2
    response=0

    while abs(response**2 - goal) >= epsilon and epsilon < goal:
        response+=step
        
    if abs(response**2 - goal) >= epsilon:
        print(f"The square root of {goal} is {result}")
    else:
        print(f"The aproximate square root is {response}")

##solutionsApproach(goal)


def binarySearch(goal):
    epsilon=0.01
    min_value=0.0
    max_value= max(1.0, goal)
    response = (max_value + min_value) /2

    while abs(response**2 - goal) >= epsilon:
        if response**2 <goal:
            min_value=response
        else : 
            max_value=response

        response = (max_value + min_value) /2

    print(f"The square root of {goal} is {response}")

##binarySearch(goal)

presentation = "Welcome to the program to take out the square root of a whole number :)  \n"
print(presentation.center(10,"-"))

goal = int(input("Please enter the number of which you wish to calculate the square root: "))

print("""Which option do you prefer?"
            [1]. Exhaustive Enumeration
            [2]. Solutions Approach
            [3]. Binary Search
            [4]. Exit""")


option = int(input(": "))

if option==1:  
    exhaustiveEnumeration(goal)

elif option==2:  
    solutionsApproach(goal)

elif option==3:  
    binarySearch(goal)

elif option==4:  
    print ("Bye Bye :)")
