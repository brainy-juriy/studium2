# Шекспир - 1564
# Эйнштейн - 1879
# Ганди - 1917
# Ньютон - 1643
# Донской - 1350
while True:
 answer = input('год рождения Уильяма Шекспира:')
 answer = int(answer)
 if answer == 1564:
     print(1)
 else:
     print(-1)

 answer = input('год рождения Альберта Эйнштейна:')
 answer = int(answer)
 if answer == 1879:
       answer = str('правильно')
 if answer != 1879:
       answer = str('неправильно')

 answer = input('год рождения Индиры Ганди:')
 answer = int(answer)
 if answer == 1917:
       answer = str('правильно')
 if answer != 1917:
       answer = str('неправильно')

 answer = input('год рождения Исаака Ньютона:')
 answer = int(answer)
 if answer == 1643:
       answer = str('правильно')
 if answer != 1643:
       answer = str('неправильно')

 answer = input('год рождения Дмитрия Донского:')
 answer = int(answer)
 if answer == 1350:
       answer = str('правильно')
 if answer != 1350:
       answer = str('неправильно')




 answer = input('Будем играть снова?:')

 while answer == 'да':

  answer = input('год рождения Уильяма Шекспира:')
  answer = int(answer)
 if answer == 1564:
    t = 1
 answer = input('год рождения Альберта Эйнштейна:')
 answer = int(answer)
 if answer == 1879:
    t = 2
 answer = input('год рождения Индиры Ганди:')
 answer = int(answer)
 if answer == 1917:
    t = 3
 answer = input('год рождения Исаака Ньютона:')
 answer = int(answer)
 if answer == 1643:
    t = 4
 answer = input('год рождения Дмитрия Донского:')
 answer = int(answer)
 if answer == 1350:
    t = 5
    print(t)
    break
