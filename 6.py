#This problem was asked by Facebook.

#Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

#For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

#You can assume that the messages are decodable. For example, '001' is not allowed.

#If the length of the message is odd, then the length of the decoded message will be odd

import re
import math
from itertools import combinations

#alphabet mapping to corresponding number
mapping = {
    "1" :"a",  "2" :"b",  "3" :"c", "4":"d", "5" :"e", "6" :"f", "7":"g",
    "8" :"h", "9" :"i", "10" :"j", "11" :"k", "12" :"l", "13" :"m", "14" :"n",
    "15" :"o", "16" :"p", "17" :"q", "18" :"r", "19" :"s", "20" :"t", "21" :"u",
    "22" :"v", "23" :"w", "24" :"x", "25" :"y", "26" :"z"
}

def find_all_occurrences(string, pattern):
    matches = re.finditer(pattern, string)
    positions = [match.span() for match in matches]
    return positions

message = "11223"
confirmed = [mapp for mapp in mapping if mapp in message]
print(confirmed)

MAX = len(message)
MIN = math.ceil(len(message)/2)

print(f"Min: {MIN} , Max: {MAX}")

print(message)
combos = {}
# span adds one to the iterator
for each in confirmed:
    print(f"Each {each}")
    temp1 = find_all_occurrences(message, each)
    if len(each) == 1:
        temp1 = [x[0] for x in temp1]
    
    print(f"temp1: {temp1}")

    


    
#messages, num_subs = re.subn(char, mapping[char], messages)
# print(f"Replaced! --> {num_subs} times")
# print(f"Message was changed to --> {messages}")

# 1-2 in length
# all possible combinations - singles and doubles mixed

    