import random

# 1-ші тапсырма
a = [random.randint(1, 100) for _ in range(10)]
print("Массив a:", a)

# Тек тақ сандарды таңдау
odd_numbers = [x for x in a if x % 2 == 1]

if odd_numbers:
    max_odd = max(odd_numbers)
    print("Максимум тақ сан:", max_odd)
else:
    print("Массивте тақ сан жоқ")

# 2-ші тапсырма
A = [[random.randint(1, 50) for _ in range(4)] for _ in range(4)]
print("\nМатрица A:")
for row in A:
    print(row)

# Қосымша (жанама) диагональ → индекстері i+j = n-1
n = 4
additional_diag = [A[i][n - 1 - i] for i in range(n)]
print("Қосымша диагональ элементтері:", additional_diag)

max_additional = max(additional_diag)
print("Қосымша диагональдағы ең үлкен элемент:", max_additional)