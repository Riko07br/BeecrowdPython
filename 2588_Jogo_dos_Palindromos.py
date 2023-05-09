respostas = []

while True:
    try:
        entrada = input()
    except EOFError:
        break    

    #dicionario para guardar a quant de repeticoes
    repeticoes = {}
    for l in entrada:
        if l in repeticoes:
            repeticoes[l] += 1
        else:
            repeticoes[l] = 1

    #pegar a quant de impares
    impares = 0
    for n in repeticoes.values():
        if n % 2 != 0:
            impares += 1
            pass
  
    #ver se quantidade de impares e impar ou par  
    if impares != 0:
        palindromos = impares - 1 if impares % 2 == 0 else impares - 1
        respostas.append(palindromos)
    else:
        respostas.append(0)

for p in respostas:
    print(p)
