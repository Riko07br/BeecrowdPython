casos = int(input())
respostas = []

for i in range(casos):

    #vai salvar os pontos no [0], o saldo de gols no [1] e gols fora de casa no [1]
    time1 = [0]*3
    time2 = [0]*3
    
    for j in range(2):
        jogo = input().strip(" ").split("x")
        jogo = [int(k) for k in jogo]
        
        #vai inverter o placar do segundo jogo para reusar a mesma logica
        if j == 1:
            jogo.reverse()

        #adiciona as pontuacoes nas tuplas
        if jogo[0] > jogo[1]:
            time1[0] += 3
        elif jogo[0] < jogo[1]:
            time2[0] += 3
        else:
            time1[0] += 1
            time2[0] += 1
        
        #saldo de gols
        time1[1] += jogo[0] - jogo[1]
        time2[1] += jogo[1] - jogo[0]

        #gols fora de casa
        if j == 1:
            time1[2] = jogo[0]
        else:
            time2[2] = jogo[1]
    
    placarFoiDecisivo = False

    #verifica se a pontuacao da a vitoria pra alguem
    for p in range(3):
        if time1[p] > time2[p] or time1[p] < time2[p]:
            respostas.append("Time 1" if time1[p] > time2[p] else "Time 2")
            placarFoiDecisivo = True
            break
        
    if not placarFoiDecisivo:
        respostas.append("Penaltis")    

for i in respostas:
    print(i)