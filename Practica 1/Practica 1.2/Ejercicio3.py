import re

text = input()
text = re.sub(r"\b(\d{4})-(\d{2})-(\d{2})\b",r'\3.\2.\1' , text)

print(text)

