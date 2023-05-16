celulas = int(input())

bombas = []
for i in range(celulas):
    bombas.append(int(input()))  
    pass

tabuleiro = [0] * celulas

for i in range(celulas):

    if bombas[i] == 0:
        continue

    tabuleiro[i] += 1
    
    if i > 0:
        tabuleiro[i-1] += 1
        
    if i < celulas - 1:
        tabuleiro[i+1] += 1


for i in range(celulas):
    print(tabuleiro[i])