#Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#Пример:
#A = 3; B = 5 -> 243 (3?)
# A = 2; B = 3 -> 8

a = int(input("Введите число A "))
b = int(input("Введите степень числа B "))


def func(a, b):
    if b == 0:
        return 1

    return a* func(a, b - 1)
    

print(f"Число A в степени B равно : {func(a, b)}")