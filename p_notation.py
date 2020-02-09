import sys
notation = str(input('Введите польскую нотацию двух положительных чисел '))
notation_list = notation.split()

class InvalidInputError(Exception):
    def __init__(self, text):
        self.text = text
        
class PolishNum():
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return other + self.num

    def __sub__(self, other):
        return other - self.num

    def __mul__(self, other):
        return other * self.num
    
    def __truediv__(self, other):
        return other / self.num  


try:
    first_num = notation_list[1]
    operation = notation_list[0]
    second_num = notation_list[2]
    if len(notation_list) > 3:
        raise InvalidInputError('Некорректный ввод. Введите знак и 2 числа')
    available_op_list = ['+', '-', '*', '/']
    assert operation in available_op_list , 'Вы ввели неверный знак'
except IndexError:
    print('Введено 1 число')
    sys.exit()
except InvalidInputError as bar:
    print(bar)
    sys.exit()
except AssertionError as ae:
    print(ae)
    sys.exit()

first = PolishNum(first_num)
second = PolishNum(second_num)

try:
    a = int(first.num)
    b = int(second.num)
except ValueError:
    print('Введено неправильное значение')
    sys.exit()
if operation == '+':
    sum = a + b
    print(sum)
elif operation == '-':
    sub = a - b
    print(sub)
elif operation == '*':
    mul = a * b
    print(mul)
elif operation == '/':
    try:
      div = a / b
      print(div)
    except ZeroDivisionError:
        print('Деление на ноль')
        