'''Write a program (using functions!) that asks the user for a long string containing 
multiple words. Print back to the user the same string, except with the words in 
backwards order.'''

sentence = input("Enter a sentence: ")
words = sentence.split()
words.reverse()
result = " ".join(words)
print(result)