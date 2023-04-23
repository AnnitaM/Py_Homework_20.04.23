# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("Enter A: "))
b = int(input("Enter B: "))

def a_pow_b(a, b):
    if b > 0:
        return a * a_pow_b(a, b-1)
    else:
        return 1

result = a_pow_b(a,b)
print("result = ", result)