
def foo(a):
        x=int(a**0.5)
        print(x)
        for i in range(2,x+1):
            if a % i != 0:
                pass
            else:
                print("Число", a, "непростое!:)")
                return
        print("Число", a, "простое!:)")

try:
    number=int(input("Введите целое число:"))
    foo(number)
except ValueError:
    print("ВЫ ВВЕЛИ НЕ ЧИСЛО!!!")
