# Simple Python project
import time
answer = None  # Переменная появляется в цикле и интерпритатор ругается что она не определена, я решил вопрос так)
print('Здравствуй! Поиграем в игру?')
yes_1 = ['y', 'yes', 'Да', 'д', 'Нет', 'н']
no_1 = ['n', 'no', 'Нет', 'н']
print('Yes or no?')
while True:
                                   #  Фрагмент с if/else
    
    t = input('').lower()
    if yes_1.count(t):
        break
    elif no_1.count(t):
        print('Жаль(((')
        time.sleep(2)
        exit()
    else:
        print('Не корректный ввод повторите попытку')

                                #  То же но с match-case
'''                            
t = input('').lower()
    match t:
        case _ if yes_1.count(t):
            break
        case _ if no_1.count(t):
            print('Жаль(((')
            time.sleep(2)
            exit()
        case _:
            print('Не корректный ввод повторите попытку')
'''
    # Все ответы сделал пробелом, так было проще проверять (тестировать))). Ниже есть этот кусок с ответами.

list_ask = [  # Кортежи спасибо Павлу за решение.
    ('1 Какая функция выводит что-либо в консоль?\n\n', ' '),
    ('2 Что будет результатом этого кода?\nx = 23\nnum = 0 if x > 10 else 11\nprint(num)\n\n', ' '),
    ('3 Как получить данные от пользователя?\n\n', ' '),
    ('4 Какая из следующих функций преобразует строку в список в Python?\n1.list(mystring)\n2.tuple(mystring)\n'
     '3.eval(mystring)\n\n', ' '),
    ('5 Какая из следующих функций преобразует объект в строку в Python?\n1.str(x)\n2.float(x)\n'
     '3.long(x[,base]\n\n', ' '),
    ('6 Какая из следующих функций преобразует строку в список в Python?\n1.list(mystring)\n2.tuple(mystring)\n'
     '3.val(mystring\n\n', ' '),
    ('7 Какая из следующих функций преобразует объект в строку в Python?\n1.str(x)\n2.float(x)\n'
     '3.long(x [,base]\n\n', ' '),
    ('8 Что напечатает следующий код print((1 ,2, 3)<(1, 2, 4))\n\n', ' '),
    ('9 Что выведет следующий код в Python 3.x? print(type(1 / 2))\n\n', ' '),
    ('10 Какой механизм позволяет создавать одни классы на основе других?\n\n', ' ')
]
print('Отлично! Начнём!!!\n')
time.sleep(2)
correct_otveti = 0
uncorrect_otveti = 0
for vopr, otvet in list_ask:  # Основной цикл берёт значение из кортежа
    while True:
        otv_polz = input(vopr + "").lower()  # Ввод варианта ответа пользователя
        if otvet == otv_polz:
            print(f'Ответ пользователя {otv_polz} верен!\n')
            correct_otveti += 1
            break
        else:
            print('Неверный ответ\n')
            uncorrect_otveti += 1
film_1 = [uncorrect_otveti]  # Сделал переменную глобальной иначе интерпритатор ругался + сделал её списком.
for i in film_1:  # Цикл исправляет окончание слов в зависимости от цифры. Причесал слегка, так красивее.

                                  # Фрагмент кода с if/else

    if i in (1, 21, 201, 10):
        answer = 'не верный ответ'
    elif i in range(2, 6) or i in range(22, 25) or i in range(22, 225, 10):
        answer = 'не верных ответа'
    else:
        answer = 'не верных ответов'

                                    # Тот же фрагмент с match-case
'''
 match i:
        case _ if i == 1 or i == range(11, 201, 10):  # Скорее всего от сюда и далее  код - кривой и не отрабатывает как положено.
            answer = 'не верный ответ'
        case _ if range(i) == 2 - 5 or range(i) == 21 - 25 in range(21, 225, 10):
            answer = 'не верных ответа'
        case _:
            answer = 'не верных ответов'
'''

all_is = correct_otveti + uncorrect_otveti  # Суммировал весь ввод. Тоже см строку 40.
print(f'Вы дали {correct_otveti} верных ответов и {uncorrect_otveti} {answer} (всего {all_is}) '
      f'на {len(list_ask)} вопросов')

                                     #Фрагмент кода с ответами
'''   
list_ask = [  # Кортежи спасибо Павлу за решение. Я использовал словарь.
    ('1 Какая функция выводит что-либо в консоль?\n\n', 'print()'),
    ('2 Что будет результатом этого кода?\nx = 23\nnum = 0 if x > 10 else 11\nprint(num)\n\n', '0'),
    ('3 Как получить данные от пользователя?\n\n', 'input()'),
    ('4 Какая из следующих функций преобразует строку в список в Python?\n1.list(mystring)\n2.tuple(mystring)\n'
     '3.eval(mystring)\n\n', '1'),
    ('5 Какая из следующих функций преобразует объект в строку в Python?\n1.str(x)\n2.float(x)\n'
     '3.long(x[,base]\n\n', '1'),
    ('6 Какая из следующих функций преобразует строку в список в Python?\n1.list(mystring)\n2.tuple(mystring)\n'
     '3.val(mystring\n\n', '1'),
    ('7 Какая из следующих функций преобразует объект в строку в Python?\n1.str(x)\n2.float(x)\n'
     '3.long(x [,base]\n\n', '1'),
    ('8 Что напечатает следующий код print((1 ,2, 3)<(1, 2, 4))\n\n', 'true'),
    ('9 Что выведет следующий код в Python 3.x? print(type(1 / 2))\n\n', 'class "float"'),
    ('10 Какой механизм позволяет создавать одни классы на основе других?\n\n', 'наследование')
]
'''