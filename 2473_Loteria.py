
aposta = [int(i) for i in input().split(" ")]
sorteio = [int(i) for i in input().split(" ")]

acertos = 0

for i in aposta:
    if i in sorteio:
        acertos += 1

if acertos == 3:
    print("terno")
elif acertos == 4:
    print("quadra")
elif acertos == 5:
    print("quina")
elif acertos == 5:
    print("sena")
else:
    print("azar")