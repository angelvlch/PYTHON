import re
def foo(a):
    if isinstance(a,list):
        word = re.findall('[a-zA-Z]+', str(a))
        word=''.join(word)
        print("1.Длина слов в списке ",a," равно:", len(word))
    elif isinstance(a,tuple):
        word = re.findall('[a-zA-Z]+', str(a))
        digit=re.findall('[0-9]+', str(a))
        print("\n2.Кол-во букв в кортеже ", a, " равно:", len(''.join(word)))
        print("2.Кол-во цифр в кортеже ",a,"равно ",len(''.join(digit)))
    elif isinstance(a,int) or isinstance(a,float):
        a=str(a)
        print("\n3.Число",a,"в обратном порядке ",end='')
        for i in range(len(a)-1,-1,-1):
            print(a[i],end='')
    elif isinstance(a,str):
        sum=0
        for i in range(len(a)):
            if a[i].isdigit():
                sum+=int(a[i])
        print("\n\n4.Сумма всех цифр в строке\n",a,"\nравна ",sum)
a=["fty",4,"45bn","-=","word1"]
b=(1,'45',"Hi!7-",' ')
c=42.195
v="2Hello!I'm Angelina, i'm 18 ye.1"
foo(a)
foo(b)
foo(c)
foo(v)