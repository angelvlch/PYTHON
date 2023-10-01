try:
    number = int(input("Введите целое число: "))
    print("Введенное число:", number)
except:
    print("Вы ввели не целое число")
finally:
    print("Блок try завершил выполнение")
print("Завершение программы")