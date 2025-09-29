try:
    result = 10 // 2
    print("Результат деления:", result)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
finally:
    print("Этот блок выполняется всегда")

try:
    result = 10 / 0
    print("Результат деления:", result)
except ZeroDivisionError:
    print("На ноль делить нельзя!")
finally:
    print("Этот блок выполняется всегда")