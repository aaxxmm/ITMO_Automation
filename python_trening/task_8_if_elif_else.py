num_float = 3
if num_float > 0:
    print('Положительное число')
elif num_float == 0:
    print('Ноль')
else:
    print('Число отрицательное')

num = 1
permit_print = True
if num > 0 and permit_print:
    print('num - положительное число')
elif not permit_print:
    print('Печать запрещена')


god = 10
if 1 <= god <= 4:
    print('Bakalavr')
elif 5 <= god <= 6:
    print('magist')
elif 7 <= god <= 8:
    print('aspirant')
else:
    print('vvedite korrectnuy god')



a = 101
if a > 100 or a < -100:
    print('-')
else:
    print('+')