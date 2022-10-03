# Шекспир - 1564
# Эйнштейн - 1879
# Ганди - 1917
# Ньютон - 1643
# Донской - 1350

right = 0  # правильный ответ
wrong = 0  # неправильный ответ

answer = input('Будем играть?:')
while answer == 'да':

  answer = input('год рождения Уильяма Шекспира:')
  answer = int(answer)
  if answer == 1564:
     print('правильно')
     right += 1  # счетчик правильных ответов
  else:
     print('неправильно')
     wrong += 1  # счетчик неправильных ответов


  answer = input('год рождения Альберта Эйнштейна:')
  answer = int(answer)
  if answer == 1879:
     print('правильно')
     right += 1
  else:
     print('неправильно')
     wrong += 1


  answer = input('год рождения Индиры Ганди:')
  answer = int(answer)
  if answer == 1917:
     print('правильно')
     right += 1
  else:
     print('неправильно')
     wrong += 1


  answer = input('год рождения Исаака Ньютона:')
  answer = int(answer)
  if answer == 1643:
     print('правильно')
     right += 1
  else:
     print('неправильно')
     wrong += 1


  answer = input('год рождения Дмитрия Донского:')
  answer = int(answer)
  if answer == 1350:
     print('правильно')
     right += 1
  else:
     print('неправильно')
     wrong += 1

  print('количество правильных ответов:', right)
  print('количество неправильных ответов:', wrong)
  print('процент правильных ответов:', int((right)*100/5))
  print('процент неправильных ответов:', int((wrong)*100/5))

  answer = input('Будем играть снова?:')
  if answer == 'нет':

   break

