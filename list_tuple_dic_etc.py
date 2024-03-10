#Program to compute the sum of integers in a list
numbers = input("Enter a list of integers, separated by spaces: ").split()
numbers = [int(num) for num in numbers]
sum_of_numbers = sum(numbers)
print("Sum of the numbers:", sum_of_numbers)

#Program to print each book name from a tuple on a separate line:
favorite_books = ("Book 1", "Book 2", "Book 3", "Book 4", "Book 5")
for book in favorite_books:
    print(book)

#Program to store and print information about a person using a dictionary:
person = {}
person['name'] = input("Enter the person's name: ")
person['age'] = input("Enter the person's age: ")
person['favorite_color'] = input("Enter the person's favorite color: ")
print("Person information:", person)

#Program to create a new set containing common elements from two sets:
set1 = set(input("Enter elements for set 1, separated by spaces: ").split())
set2 = set(input("Enter elements for set 2, separated by spaces: ").split())
common_elements = set1.intersection(set2)
print("Common elements:", common_elements)

#Program to create a new list of words with an odd number of characters using list comprehension:
word_list = input("Enter a list of words, separated by spaces: ").split()
odd_length_words = [word for word in word_list if len(word) % 2 != 0]
print("Words with odd length:", odd_length_words)