first = input('Введите первое число: ')
second = input('Введите второе число: ')
third = input('Введите третье число: ')
if first == second and first == third and second == third: # все три числа равны
    print('3')
elif first == second or first == third and second != third:
    print('2')
elif second == first or second == third and first != third:
    print('2')
else:                                                      # не равные числа
    print('0')