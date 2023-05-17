respostas = []

while True:
    jogadas = int(input())

    if jogadas == 0:
        break

    moedas = input().split(" ")

    partidas = {"m": 0, "j": 0}

    for i in range(jogadas):
        
        if moedas[i] == "0":
            partidas["m"] += 1
        else:
            partidas["j"] += 1

    respostas.append(partidas)

for r in respostas:
    print(f'Mary won {r["m"]} times and John won {r["j"]} times')