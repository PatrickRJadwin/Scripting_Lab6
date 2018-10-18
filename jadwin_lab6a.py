import math as m
for i in range(5):
    for x in range(5):
        b = i ** 2 + x ** 2
        m.sqrt(b)
        if b <= 20:
            print(str(i) + '^2 + ' + str(x) + '^2 = ' + str(b))

