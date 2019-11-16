import csv
from operator import itemgetter


# -*- coding: UTF-8 -*-
"""Resume Analysis Module."""

import os
import string

# Counter is used later in the program
from collections import Counter

# Paths
resume_path = "resume.md"

# Skills to match
REQUIRED_SKILLS = {"excel", "python", "mysql", "statistics"}
DESIRED_SKILLS = {"r", "git", "html", "css", "leaflet"}

# function to load a file
def load_file(filepath):
    """Helper function to read a file and return the data."""
    with open(filepath, "r") as resume_file_handler:
       return  resume_file_handler.read().lower().split()

# Grab the text for a Resume
word_list = load_file(resume_path)

# Create a set of unique words from the resume
resume = set()
# for w in word_list:
#     resume.add(w)



# Remove trailing punctuation from words
for token in word_list:
    resume.add(token.split(',')[0].split('.')[0])

# Remove Punctuation that were read as whole words
punctuation = set(string.punctuation)
resume = resume - punctuation
print(resume)

# Calculate the Required Skills Match using Set Intersection
print("REQUIRED SKILLS")
print("=============")
print(resume & REQUIRED_SKILLS)


# Calculate the Desired Skills Match using Set Intersection
print("DESIRED SKILLS")
print("=============")
print(resume & DESIRED_SKILLS)

# Resume Word Count
# ==========================
# Initialize a dictionary with default values equal to zero
word_count = {}.fromkeys(word_list, 0)

# Loop through the word list and count each word.
for word in word_list:
    word_count[word] += 1
print(word_count)

# Using collections.Counter
word_counter = Counter(word_list)
print(word_counter)

# Comparing both word count solutions
print(word_count == word_counter)

# Top 10 Words
print("Top 10 Words")
print("=============")

# Don't worry about the underscore in front of _word_count
# It is just convention for internal use only
# More info here: https://dbader.org/blog/meaning-of-underscores-in-python

# Clean Punctuation
_word_count  = len(resume - punctuation) #YOUR CODE HERE hint:
for w in resume:
    if w in punctuation :
        resume.remove(w)
# Hint: return only words that are not in string.punctuaton
# Hint: consider using a list comprehension

# Clean Stop Words
stop_words = ["and", "with", "using", "##", "working", "in", "to"]
#_word_count = #YOUR CODE HERE#
remove = []
for w in resume :
     if w in stop_words:
         remove.append(w)
for w in remove:
    resume.discard(w)
_word_count = len(resume)

# Sort words by count and print the top 10
sorted_words =  {}
# sorted_words = sorted(word_count, key=itemgetter(1),reverse = True)
# sorted_words = dict( sorted(word_count.items(, key=operator.itemgetter(0),reverse=True))
sorted_words = sorted(word_count.items(), key=itemgetter(1),reverse = True)
wc = 0
for s in sorted_words:
    wc += 1
    print(s)
    if wc > 9:
      break


