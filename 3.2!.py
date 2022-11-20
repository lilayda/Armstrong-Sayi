print('''Armstrong Sayı Programı''')

a = input('bir sayı giriniz:')
b = list(a)
c = len(a)
d = 0
k = int(a)
for i in b:
    d += int(i)**c
    if (d == int(a)):
        print('{} bir armstrong sayıdır.'.format(a))
if (d != int(a)):
    print('{} bir armstrong sayı değildir.'.format(a))