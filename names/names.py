import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# What is the runtime complexity of this code?
# Six seconds is an eternity so you've been tasked with speeding up the code. 
# Can you get the runtime to under a second? Under one hundredth of a second?

class NamesBST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = NamesBST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = NamesBST(value)
            else:
                self.right.insert(value)

    def contains(self, target):
        if target == self.value:
            return True
        if target >= self.value:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

# Runtime complexity 0(n)
names_search_tree = NamesBST(names_1[0])
for name in names_1:
    names_search_tree.insert(name)

# Runtime Complexity 0(log n)
for name in names_2:
    if names_search_tree.contains(name):
        duplicates.append(name)

# Runtime: 0.1092 seconds
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.

# Runtime: 1.3219 seconds
start_time_2 = time.time()
stretch_duplicates = [n for n in names_1 if n in names_2]
end_time_2 = time.time()
print (f"{len(stretch_duplicates)} duplicates:\n\n{', '.join(stretch_duplicates)}\n\n")
print (f"runtime: {end_time_2 - start_time_2} seconds")