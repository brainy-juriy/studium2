import sys
answer = input('год рождения А.С.Пушкина:')
answer = int(answer)
if answer == 1799:
     answer = input('день рождения А.С.Пушкина:')
else:
    print('неверный год рождения') + sys.exit()
answer = int(answer)
if answer == 6:
    print('верно')
else:
    print('неверный день рождения')
