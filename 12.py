# Калькулятор точек
# Вам нужно написать калькулятор, принимающий на вход строки.
# Точки будут представлять число в уравнении. С одной стороны будут точки,
# оператор и ещё точки после оператора.
# Точки и оператор будут разделены одним пробелом.
#
# Вот следующие допустимые операторы:
#
# +Добавление
# -Вычитание
# *Умножение
# //Целочисленное деление
# Ваша работа (задача)
# Вам нужно будет вернуть строку, содержащую столько точек,
# сколько возвращает уравнение. Если результат равен 0, верните пустую строку.
# При вычитании первое число всегда будет больше или равно второму.


# def calculator(txt):
#     lst = txt.split()
#     x = len(lst[0])
#     y = len(lst[2])
#     z = "."
#     res = ""
#     if lst[1] == "+":
#         res += z * x + z * y
#     if lst[1] == "-":
#         res += (x - y) * z
#     if lst[1] == "*":
#         res += x * y * z
#     if lst[1] == "//":
#         res += x // y * z
#     return res
def calculator(txt):
    lst = txt.split()
    x = len(lst[0])
    y = len(lst[2])
    z = "."
    res = ""
    d = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '//': lambda x, y: x // y,
    }


print(calculator("..... + ..............."))
