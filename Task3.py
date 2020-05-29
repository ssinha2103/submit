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

#PART-A

bangalore = []
for i in calls:
    if i[0][0:5] == "(080)":
        bangalore.append(i)
bangalore_call_prefix = set()
for i in bangalore:
    if i[1][:2] == '(0':
        bangalore_call_prefix.add(i[1].split(sep=')')[0] + ')')
    elif i[1][:3]== '140':
        bangalore_call_prefix.add(i[1][:3])
    else:
        bangalore_call_prefix.add(i[1][:4])
s = list(bangalore_call_prefix)
s.sort()
print("The numbers called by people in Bangalore have codes:")
for i in s:
    print(i)







#PART-B

fixed_lines_contacted_from_bangalore = []
for i in bangalore:
    if i[1][:2] == '(0':
        fixed_lines_contacted_from_bangalore.append(i[1].split(sep=')')[0] + ')')
# print(fixed_lines_contacted_from_bangalore)
in_bangalore = 0
for j in fixed_lines_contacted_from_bangalore:
    if j[:6] == '(080)':
        in_bangalore += 1
# print(in_bangalore)
# print(len(fixed_lines_contacted_from_bangalore))

print("\n {} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
       round(in_bangalore/len(fixed_lines_contacted_from_bangalore)*100, 2)))

'''
analysis (Worst Case Big-O Notation) of my solution == O(n)
'''

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

'''
analysis (Worst Case Big-O Notation) of my solution == O(n)
'''