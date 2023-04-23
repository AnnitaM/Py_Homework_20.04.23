# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
# !!! return sum(a,b-1) + 1 - Так делать нельзя
# 2 2
# 4

a = int(input("Enter A: "))
b = int(input("Enter B: "))
def sum_a_b(a, b):
    if b == 0:
        return a
    else:
        return sum_a_b(a + 1, b - 1)

c = sum_a_b(a,b)
print("result = ", c)






