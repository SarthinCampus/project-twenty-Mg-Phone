import re

text = input()
vowels = re.findall(r'[aeiouAEIOU]', text)

for v in vowels:
    print(v)
