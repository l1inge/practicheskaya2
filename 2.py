Suma = 0
god = float(input('Введите год:'))

if (god % 4 == 0 and god % 100 != 0 or god % 400 == 0):
    fevraly = 29
    print('Високосный год: ')
else:
    fevraly = 28
    print(' Не високосный год: ')
mesac = [31, fevraly, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(len(mesac)):
    for numb in range(mesac[i]):
       numb += 1
       Suma += sum(map(int, str(numb)))
print(Suma)
