notas = []

while len(notas) < 2:
    nota = float(input())

    if nota > 10 or nota < 0:
        print("nota invalida")
        continue

    notas.append(nota)

print(f"media = {((notas[0] + notas[1]) * .5):.2f}")