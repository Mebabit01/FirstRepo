"""Write a Python program that prompts the user for a text file name 
and reads through the file line by line. 
Break each line into a list of words using the split() method, 
and build a dictionary that maps each unique word to the number of times it appears in the file.
Once the dictionary is complete, use a maximum loop to look through all of the word/count pairs to
find the most frequently occurring word
and how many times it appeared. 
Print the most common word and its count."""
import csv

name = input("Enter file name: ")
handle = open(name)
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        
bigcount = None 
bigword = None
for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)
