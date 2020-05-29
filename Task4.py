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

telemarketers = set()
outgoing_numbers = set()
incoming_numbers = set()
incoming_text = set()
outgoing_text = set()
for i in calls:
    outgoing_numbers.add(i[0])
    incoming_numbers.add(i[1])

for j in texts:
    incoming_text.add(i[0])
    outgoing_text.add(i[1])

for i in outgoing_numbers:
    if i not in incoming_numbers and i not in incoming_text and i not in outgoing_text:
        telemarketers.add(i)

s = list(telemarketers)
s.sort()
print("These numbers could be telemarketers: \n")
for i in s:
    print(i)

'''
analysis (Worst Case Big-O Notation) of my solution == O(n)
'''

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
