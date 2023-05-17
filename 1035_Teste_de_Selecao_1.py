val = input("").split(" ")

a, b, c, d = [int(v) for v in val]

if b > c and d > a and (c + d) > (a + b) and c > 0 and d > 0 and (a % 2) < 1:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')