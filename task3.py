import re

list_keys=[]
list_lessons=[]
with open("lessons.txt","r") as f:
    for i in f:
        keys=re.findall("[a-zA-Z]+[:]",i)
        keys[0]=list(keys[0])
        keys[0].remove(':')
        keys[0]="".join(keys[0])
        list_keys.append(keys[0])
        lessons=sum(list(map(int,re.findall("[0-9]+",i))))
        list_lessons.append(lessons)
    print(list_keys,list_lessons)
    SCHOOL=dict(zip(list_keys,list_lessons))
    print(SCHOOL) 
