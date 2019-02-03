# List
# Built in function

# list.reverse()
num = [1,2,3]           # List of number
num.reverse()           #`Reverse the elemt in the list
print(num)              # Output = [3, 2, 1]
print()

num = [1,2,3]                    # List of number
reverse_list = num[::-1]         # Reverse the list by printing the element of the list start from the last to the first
print(reverse_list)              # Output = [3, 2, 1]
print()

num = [1,2,3]                    # List of number
for x in reversed(num):          # Using the reversed function in for loop
    print(x)                     # Output = 3 2 1