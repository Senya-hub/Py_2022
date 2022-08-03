print("Задача 2. Кратность\n")

def count(num):
  for i in range(1, num + 1):
     print('Введите', i, 'число: ', end = '')
     number = int(input())
     list_num.append(number)

def control_divider(d, index):
    print('\n')
    summa = 0
    for i in list_num:
      if i % d == 0:
        print('Индекс числа', i, ':', index)
        summa += index
      index += 1
    return summa

n = int(input('Кол-во чисел в списке: '))
index = 0
list_num = []

count(n)
divider = int(input('\nВведите делитель: '))
s = control_divider(divider, index)
print('Сумма индексов:', s)