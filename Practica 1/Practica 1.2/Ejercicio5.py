import re
text = input()
pattern = r"\b(C\/|Calle)\s([A-ZÁÉÍÓÚÜÑ]{1}[a-záéíóúüñ]+)\,?\s+([Nn]\º?)?\s?(\d+)\,\s*(\d{5})\b"
results = re.findall(pattern, text)
for match in results:
        print(match[4]+"-"+match[1]+"-"+match[3])