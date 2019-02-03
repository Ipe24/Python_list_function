# List
# Built in function

# list.copy()
num = [1,2,3]           # List of number

new_num = num.copy()    # Copy the list to another variable
new_num.insert(0,9)     # Insert Element to the new variable
print(new_num)          # Output = [9, 1, 2, 3]

new_num.sort()          # Sort the list ascending
print(new_num)          # Output = [1, 2, 3, 9]
