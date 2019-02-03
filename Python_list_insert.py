# List
# Built in function

# list.insert(index, item)        NOTE: index is the position of the item in a list
letter = ['a','b','c']      # List of letter
letter.insert(0, 1)         # Insert the item in a specific position
print(letter)               # Output = [1, 'a', 'b', 'c']
print()

mixed = []                  # List of nothing
num = {1,2,3}               # Tuple of numbers
letter = ('a','b','c')      # Set of letter
mixed.insert(0, num)        # Insert the tuple in the list
mixed.insert(1, letter)     # Insert Set in the list
print(mixed)                # Output = [{1, 2, 3}, ('a', 'b', 'c')]
print()

