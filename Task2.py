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

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

dictionary = {}
for call in calls:
    if call[0] not in dictionary:
        dictionary[call[0]] = int(call[3])
    else:
        dictionary[call[0]] = dictionary.get(call[0]) + int(call[3])

for call in calls:
    if call[1] not in dictionary:
        dictionary[call[1]] = int(call[3])
    else:
        dictionary[call[1]] = dictionary.get(call[1]) + int(call[3])
max_time = 0
call_id = 0
for i in dictionary:
    if dictionary[i] > max_time:
        max_time = dictionary[i]
        call_id = i

print(f"{call_id} spent the longest time, {max_time} seconds, on the phone during September 2016.")

