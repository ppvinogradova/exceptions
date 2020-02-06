notation = str(input('Введите польскую нотацию двух положительных чисел '))
notation_list = notation.split()

class InvalidInputError(Exception):
    def __init__(self, text):
        self.text = text
    
try:
    first_num = notation_list[1]
    operation = notation_list[0]
    second_num = notation_list[2]
    if len(notation_list) > 3:
        raise InvalidInputError('Введено более 2х цифр')
except IndexError:
    print('Введено 1 число')
except InvalidInputError as bar:
    print(bar)

available_op_list = ['+', '-', '*', '/']
assert operation in available_op_list , 'Вы ввели неверный знак'

class polish_num():
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
    
first = polish_num(first_num)
second = polish_num(second_num)

try:
    a = int(first.num)
    b = int(second.num)
except ValueError:
    print('Введено неправильное значение')

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
        div = a
        print(a)
    except NameError:
        div = 0
        print(div)