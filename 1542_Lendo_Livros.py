respostas = []

while True:
    recebe = input()

    if recebe == "0":
        break

    lento, diasPoupados, rapido = [int(i) for i in recebe.split(" ")]
    paginas = int((lento * rapido * diasPoupados) / (rapido - lento))

    respostas.append(f"{paginas} pagina" if (paginas < 2 and paginas > -2) else f"{paginas} paginas")

for i in respostas:
    print(i)