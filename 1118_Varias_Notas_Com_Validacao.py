notaVelha = -1
pedirCalculo = False

while True:
    if pedirCalculo:
        print("novo calculo (1-sim 2-nao)")
        respCalc = int(input())

    if respCalc == 1:
        pedirCalculo = False
    elif respCalc == 2:
        break
    else:
        continue
        
    nota = float(input())

    if nota > 10 or nota < 0:
        print("nota invalida")
        continue

    if notaVelha < 0:
        notaVelha = nota
        continue

    print(f"media = {((notaVelha + nota) * .5):.2f}")
    notaVelha = -1
    pedirCalculo = True