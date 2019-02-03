# List
# Built in function

# list.count(item)
num = [1,2,3,1,3,4,5]   # List of number
a = num.count(1)        # Count how many that item occur in the list
b = num.count(3)        # Count how many that item occur in the list
print(a)                # Output = 2
print(b)                # Output = 2
print()

mixed = [{'a','b','c'},1,2,3,4,(-1,-2,-3),{'a','b','c'}]     # List of tuple, list and set
a = mixed.count({'a','b','c'})                               # count the occurrence of the item
print(a)                                                     # Output = 2