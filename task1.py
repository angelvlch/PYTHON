def is_bad_range(n,k):
    return n>k
def is_range(num,l):
    return num>len(l) or num<=0
def Range(l):
    while True:
        try:
            l[0]=int(input("Введите номер строки, с которой хотите начать копирование: "))
            l[1]=int(input("Введите  номер строки, на которой хотите завершить копирование: "))
            if is_bad_range(l[0],l[1]):
                print("Номер начала строки не может быть больше номера строки конца!")
                continue
            if is_range(l[0],content) or is_range(l[1],content):
                print("Неверно указан диапазон!")
                continue
            break
        except ValueError:
            print("ValueError\n")
            continue
def count_consonants(ll):
    ll=''.join(ll)
    ll=ll.lower()
    cons="aeyuo"
    count=0
    print(ll)
    for i in range(len(ll)):
        if ll[i].isalpha() and ll[i] not in cons:
            count+=1
    return count


with open("F1.txt","w") as f1:
    print("Enter text:\n")
    while True:
        a=input()
        if not a:
            break
        f1.write(a+'\n')

with open("F1.txt","r") as f1, open("F2.txt","w") as f2:
    content=f1.readlines()
    l=[0,0]
    Range(l)
    print("content=",content)
    content2=content[l[0]-1:l[1]]
    f2.writelines(content2)
    print("Кол-во согласных в файле F2 равно ",count_consonants(content2))



