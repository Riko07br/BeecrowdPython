
loops = int(input())

numeros = {}

for i in range(loops):
  
    numero = int(input())

    if numero in numeros:
        numeros[numero] += 1
    else:
        numeros[numero] = 1
  


sortedKeys = list(numeros.keys())
sortedKeys.sort()

for k in sortedKeys:
    print(f"{k} aparece {numeros[k]} vez(es)")