"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)
for i in texts:
    print(f"First record of texts, {i[0]} texts {i[1]} at time {i[2]}")

for j in calls:
    print(f"Last record of calls, {j[0]} calls {j[1]} at time {j[2]}, lasting {j[3]} seconds")


'''
analysis (Worst Case Big-O Notation) of my solution == O(n)
'''



"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of text, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""

'''
analysis (Worst Case Big-O Notation) of my solution == O(n)
'''
