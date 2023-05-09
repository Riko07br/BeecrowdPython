
x = int(input())
raiz = 5**.5
resposta = ((((1 + raiz) * .5)**x) - (((1 - raiz) * .5)**x)) / raiz
print(f"{resposta:.1f}")