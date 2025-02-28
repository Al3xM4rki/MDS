import re

text = input()
pattern = r"\b([a-zA-Z]{1}\.([a-zA-Z]{2,})\.(\d{4})\@alumnos\.urjc\.es)\b"
results = re.findall(pattern, text)
pattern2 = r"\b(([a-zA-Z]{1,})\.([a-zA-Z]{1,})\@urjc\.es)\b"
results2 = re.findall(pattern2, text)
for match in results:
        print("alumno " + match[1] + " matriculado en " + match[2])

for match in results2:
        print("profesor " + match[1] + " apellido " + match[2])
