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


x = {1,}
for i in texts:
    x.add(i[0])
    x.add(i[1])

for j in calls:
    x.add(j[0])
    x.add(j[1])

print(len(x)-1)

'''
analysis (Worst Case Big-O Notation) of my solution == O(n)
'''

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""

'''
analysis (Worst Case Big-O Notation) of my solution == O(n)
'''
