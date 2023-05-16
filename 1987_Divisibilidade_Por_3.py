somas = []

while True:
    try:
        line = input()
    except EOFError:
        break

    line = line.split(" ")

    loops = int(line[0])

    soma = 0
    for i in line[1]:
        soma += int(i)

    somas.append(soma)

for s in somas:
    print(f"{s} " + ('sim' if s%3 == 0 else 'nao'))