# List
# Built in function

# list.extend(argument)
num = [1,2,3,4]     # List of number
num2 = [-1,-2,-3]   # List of negative number
num.extend(num2)    # Unlike append it does not add the list inside the list It add the element of another list to the other list
print(num)          # Output = [1,2,3,4,-1,-2,-3]
print()

num = [1,2,3,4]     # List of number
num2 = (-1,-2,-3)   # Tuple of negative number
num3 = {'a','b','c'}# Set of letters
num.extend(num2)    # Add the element of Tuple
num.extend(num3)    # Add the element of Set
print(num)          # Output = [1,2,3,-1,-2,-3,'a','b','c']
print()

num = [1,2,3,4]     # List of number
num2 = [-1,-2,-3]   # List of negative number
num += num2         # Can use also the + or += to add the element of other list to another
print(num)          # Output = [1,2,3,4,-1,-2,-3]