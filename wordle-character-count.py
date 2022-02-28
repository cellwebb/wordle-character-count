import re
from collections import Counter

with open('words.txt') as f:
    words = f.read()

c = Counter(re.sub(r'[^a-z]', '', words.lower()))
print(c)
