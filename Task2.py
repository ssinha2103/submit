"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

max_time = 0
call_id = 0
for i in calls:
    y = int(i[3])
    if y > max_time:
        max_time = y
        call_id = i

print(f"{call_id[0]} spent the longest time, {max_time} seconds, on the phone during September 2016.")

'''
analysis (Worst Case Big-O Notation) of my solution == O(n)
'''

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

'''
analysis (Worst Case Big-O Notation) of my solution == O(n)
'''