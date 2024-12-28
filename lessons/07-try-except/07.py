print('Input N1:')
n1 = input()
print('Input N2:')
n2 = input()

try:
    d = int(n1) / int(n2)
    print(d)
except ZeroDivisionError:
    print("Ділення на нуль")
except TypeError:
    print("Не можна ділити рядок на рядок")
    d = int(n1) / int(n2)
    print("Переведоно в числа",d)
finally:
    print("Блок винятків завершено")

print('End!')