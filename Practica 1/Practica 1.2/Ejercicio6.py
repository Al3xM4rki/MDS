import re
text = input()
pattern = r"\d{3}\s+([a-zA-Z]+)\s+\d{7}"
pattern2 = r"\-\-\-\s+\[(\w+)\]"
pattern3 = r"([a-zA-Z]{0,}\.)?([a-zA-Z]{1,})\s+\:"
pattern4 = r"\:\s(.+)"
results = re.findall(pattern, text)
results2 = re.findall(pattern2, text)
results3 = re.findall(pattern3, text)
results4 = re.findall(pattern4, text)
i=0
for match in results:
        print("\"" + match + "\",\"" + results2[i] + "\",\"" + results3[i][1] +  "\",\"" + results4[i] +"\"")
        i += 1