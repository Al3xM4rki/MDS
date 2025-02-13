import re

text = input()
text = re.sub(r"(\d{4})-(\d{2})-(\d{2})",r'\3.\2.\1' , text)

print(text)