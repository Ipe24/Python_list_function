# List
# Built in function

# list.remove(item)
animal = ['dog','cat','pig']    # List of animal
animal.remove('pig')            # Remove item in the list
print(animal)                   # Output = ['dog', 'cat']
print()

animal = ['dog','cat','pig','parrot','pig'] # List of animal
animal.remove('pig')                        # Remove only the first instance it find
print(animal)                               # Output = ['dog', 'cat', 'parrot', 'pig']

# Removing item that is not in the list return a error
