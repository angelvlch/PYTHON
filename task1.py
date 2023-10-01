def foo(a):
        for i in range(2, a):
            if a % i != 0:
                pass
            else:
                print("Число", a, "непростое!:)")
                return
        print("Число", a, "простое!:)")



try:
    number=int(input("Введите целое число:"))
    foo(number)
except:
    print("ВЫ ВВЕЛИ НЕ ЧИСЛО!!!")
