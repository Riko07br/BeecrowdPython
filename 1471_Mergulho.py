resposta = []

while True:
    try:
        entrada = input()
    except EOFError:
        break

    entraram, sairam = [int(i) for i in entrada.split(" ")]

    placas = input().split(" ")
    placas = [int(i) for i in placas]

    morreram = ""
    for i in range(1, entraram + 1):
        if not (i in placas):
            morreram += str(i) + " "

    resposta.append("*" if (morreram == "") else morreram)

for r in resposta:
    print(r)
