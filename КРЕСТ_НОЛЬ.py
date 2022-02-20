"""
крестики-нолики 3х3
вот так будут выглядеть координаты
  1 2 3
a _ _ 0
b х _ 0
c х 0 _
Подготовительный этап
1.создать поле (_) 3 на 3, с координатами
2.предложить выбрать крестик или нолик
3. установить для компьютера крестик или нолик
Игровой цикл
4 вывести поле с координатами
5. Проверить ситуацию на поле
6. Если ходить больше некуда, выводим сообщение "ничья" и выходим из игры
7. Попросить координаты для хода
8. поставить выбранную фигуру на поле по введенным координатам
9. Проверить ситуацию на поле
10. если собраны линии по вертикали,горирзонтали или по диагонали написать победа
11. ход комьютера, координаты выбираются случайно из всего набора пустых ячеек
12. Проверить ситуацию на поле
13. если собраны линии по вертикали,горирзонтали или по диагонали написать "проиграл"
"""

from random import randint

VERTICAL_COORDINATS = ('a', 'b', 'c')
EMPTY_CHAR = '_'
field_of_play = [['_', '_', '_'],
                 ['_', '_', '_'],
                 ['_', '_', '_']]


def show_field():
    """Выводит игровое поле с координатами"""
    print(' ', '1', '2', '3')

    # отображаю игровое поле
    for i in range(3):
        print(VERTICAL_COORDINATS[i], end=" ")
        for j in range(3):
            print(field_of_play[i][j], end=" ")
        print()


user_char = input("Введите за какой знак вы будете играть (X или O) $>")
while not (user_char in ("X", "O")):
    user_char = input(f"{user_char} является недопустимым знаком введи пожалуйста X или O $>")
print(f"Вы играете {user_char}")

# if user_char == "O":
#     computer_char = "X"
# else:
#     computer_char = "O"

# Тернарный оператор
computer_char = 'O' if user_char == "X" else "X"

print(f"Компьютер играет за {computer_char}")

corret_vertical_coordinats = {"a": 0, "b": 1, "c": 2}
while True:
    show_field()

    print(f"Игрок со знаком {user_char} ВАШ ХОД!!!")
    y = input("Введите номер строки (a,b,c) $>")
    # if y == "a":
    #     y = 0
    # elif y == "b":
    #     y = 1
    # elif y == "c":
    #     y = 2

    x = int(input("Введите номер стобца (1,2,3) $>"))

    field_of_play[corret_vertical_coordinats[y]][x - 1] = user_char
    show_field()

    # if is_draw(field_of_play) print(ничья) break
    # x,y = get_user_position(field_of_play)
    # field_of_play[y][x] = user_char
    # if is_win(user_char, field_of_play):
    #     print('you win')
    #     break
    #

    # x, y = get_computer_position(field_of_play)
    #
    # field_of_play[y][x] = computer_char
    # if is_win(computer_char, field_of_play):
    #     print('you lose')
    #     break
    break
