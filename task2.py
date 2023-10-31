import re

with open("F3.txt","r") as f:
    s=f.readlines()

d = {}
for i in s:
    digit = sum(list(map(int, re.findall("[0-9]+", i))))
    name = ''.join(re.findall("[a-zA-Z]+", i))
    d[name] = digit / 5
print(d)
print("Students with <6:")
for i in d:
    if d[i] < 6:
        print(i, ":", d[i])
