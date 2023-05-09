resposta = []

while True:
    try:
        entrada = input()
    except EOFError:
        break

    entrada = entrada.split(" ")
    entraram = int(entrada[0])
    sairam = int(entrada[1])

    placas = input().split(" ")
    placas = [int(i) for i in placas]

    morreram = []

    for i in range(1, entraram + 1):
        if not (i in placas):
            morreram.append(i)

    if len(morreram) == 0:
        resposta.append("*")    
    else:
        morreram = list(morreram)
        morreram.sort()
        resposta.append(morreram)

for i in resposta:
    if i == "*":
        print("*")
        continue

    linhaResposta = ""
    for j in i:
        linhaResposta += str(j) + " "
    pass
    print(linhaResposta)
