while True:
    answer = input('год рождения А.С.Пушкина:')
    answer = int(answer)
    if answer == 1799:
        while True:
           answer = input('день рождения А.С.Пушкина:')
           answer = int(answer)
           if answer == 6:
               break
        break
print('верно')


