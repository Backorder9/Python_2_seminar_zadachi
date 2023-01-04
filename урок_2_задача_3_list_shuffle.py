'''
Реализуйте алгоритм перемешивания списка.
НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE,
максимум использование библиотеки Random для и получения случайного int.
'''
import random
week = ['понеденьник', 'вторник', 'среда',
        'четверг', 'пятница', 'суббота', 'воскресенье']
shuffled_week = []
while len(shuffled_week) < 7:
    day = random.choice(week)
    if day not in shuffled_week:
        shuffled_week.append(day)
print('Дни недели в прямом порядке:')
print(week)
print()
print('Дни недели в случайном порядке:')
print(shuffled_week)
