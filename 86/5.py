number = int(input("Введите положительное целое число:"))
pos = int(input("Введите позицию разряда от 1 до N: "))

np = (number // 10*(pos-1)) % 10

print(f"Цифра в {pos} разряде равна {np}")