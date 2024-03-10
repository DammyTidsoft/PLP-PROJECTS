my_list = []  # Create an empty list called my_list
my_list.append(10)  # Append 10 to my_list
my_list.append(20)  # Append 20 to my_list
my_list.append(30)  # Append 30 to my_list
my_list.append(40)  # Append 40 to my_list
my_list.insert(1, 15)  # Insert 15 at the second position in the list
my_list.extend([50, 60, 70])  # Extend my_list with [50, 60, 70]
my_list.pop()  # Remove the last element from my_list
my_list.sort()  # Sort my_list in ascending order
index_of_30 = my_list.index(30)  # Find the index of the value 30 in my_list

print("my_list:", my_list)
print("Index of 30:", index_of_30)