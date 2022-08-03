print('Задача 3. Собачьи бега\n')

def count_dogs(d):
  big = 0
  small = 0
  dogs_list = []
  for n in range(d):
    print('Введите очки', n + 1, 'coбаки:', end = ' ')
    num = int(input())
    dogs_list.append(num)

    if dogs_list[n] > big:
      big = num
      index_big = n
    elif dogs_list[n] < small:
      small = num
      index_small = n
  dogs_list[index_big], dogs_list[index_small] =  dogs_list[index_small], dogs_list[index_big]
  return dogs_list



dogs = int(input('Введите кол-во собак: '))
print(count_dogs(dogs))


