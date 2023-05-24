while True:
    recebe = input().split(" ")
    x, y = [int(i) for i in recebe]

    if x == 0 or y == 0:
        break

    quadrante = "primeiro" if y > 0 else "quarto"

    if x < 0:
        quadrante = "segundo" if y > 0 else "terceiro"

    print(quadrante)