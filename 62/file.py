# 10 
v0 = float(input("Начальная скорость: "))
a = float(input("Ускорение: "))
t = float(input("Время: "))

s = v0 * t + a * t**2 / 2

print("Пройденный путь:", s)