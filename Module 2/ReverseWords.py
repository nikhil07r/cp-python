# print the reverse of the words in a given string .
string = input("Enter a string: ")
words = string.split()
reverse = ' '.join(reversed(words))
print("Reversed words:", reverse)