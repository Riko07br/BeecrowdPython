testes = int(input())

respostas = []

for i in range(testes):
    numero = int(input())

    iteracoes = [0, 0]
    old = 0
    new = 1
    newer = 0
    for i in range(2, numero + 1):
        newer = new + old
        old = new
        new = newer    
        iteracoes.append(iteracoes[i-1] + iteracoes[i-2] + 2)    
    pass
    
    respostas.append("fib({}) = {} calls = {}".format(numero, iteracoes[-1], newer))
    pass
for i in respostas:
    print(i)