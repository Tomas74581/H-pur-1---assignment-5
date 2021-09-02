# Algorithm
# Make an algorithm that takes positive integers repeatively until a negative value is entered
# When a negative value is entered, the maximum positive integer entered by the user should be printed 

# Output should say The maximum is (max integer)

num_int = 0
max_int = 0
while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int
# Fill in the missing code

print("The maximum is", max_int)    # Do not change this line
