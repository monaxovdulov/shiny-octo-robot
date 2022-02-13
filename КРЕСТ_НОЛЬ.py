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

print('', '1', '2', '3')

field_of_play = [['_', '_', '_'],
                 ['_', '_', '_'],
                 ['_', '_', '_']]

for i in range(3):
    print(VERTICAL_COORDINATS[i], end="")
    for j in range(3):
        print(field_of_play[i][j], end=" ")
    print()


