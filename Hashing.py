#Hashing refers to the process of generating a fixed-size output from an input of variable
#size using the mathematical formulas known as hash functions.
#This technique determines an index or location for the storage of an item in a data structure.

class HashList:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        # A simple hash function that uses modulo to map integers to indices
        return key % self.size

    def insert(self, element):
        index = self.hash_function(element)
        if self.table[index] is None:
            self.table[index] = [element]
        else:
            # Collision handling (simple chaining)
            self.table[index].append(element)

    def search(self, target):
        index = self.hash_function(target)
        if self.table[index] is not None:
            # Search for the target in the list at the hashed index
            if target in self.table[index]:
                return True  # Element found

        return False  # Element not found

# Example usage
hash_list = HashList(size=10)
hash_list.insert(42)
hash_list.insert(18)
hash_list.insert(7)

# Searching for elements
result_42 = hash_list.search(42)
result_99 = hash_list.search(99)

print("Is 42 in the list?", result_42)  # Output: True
print("Is 99 in the list?", result_99)  # Output: False