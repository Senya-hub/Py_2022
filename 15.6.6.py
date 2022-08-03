print('Задача 6. Анализ слова\n')

word = list(input('Введите слово: '))
count = 0
summ = 0

for num in range(len(word)):
  for sym in word:
    if word[num] == sym:
      count += 1
  if count == 1:
    summ += 1
  count = 0
print('Количество уникальных букв:', summ)