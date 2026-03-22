import io
try:
    with open('requirements.txt', 'r', encoding='utf-16le') as f:
        lines = f.readlines()
except UnicodeError:
    with open('requirements.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

filtered = []
for line in lines:
    lower_line = line.lower()
    if 'win32' not in lower_line and 'awsebcli' not in lower_line:
        filtered.append(line)

with open('requirements.txt', 'w', encoding='utf-8') as f:
    for line in filtered:
        f.write(line)
print("Cleaned requirements.txt")
