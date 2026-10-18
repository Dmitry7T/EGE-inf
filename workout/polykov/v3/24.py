import re

f = open("24.txt").read().strip()

pattern = r"(?=(A[^AD]*D|D[^AD]*A))"

max_len = 0
for match in re.finditer(pattern, f):
    length = len(match.group(1))
    if length > max_len:
        max_len = length

print(max_len)