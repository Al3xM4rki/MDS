import re

text = input()
pattern = "\\b(E?(-|\\s|)\\d{4}(-|\\s|)[A-Z]{3})\\b"
results = re.findall(pattern, text)
for match in results:
 print(match[0])
