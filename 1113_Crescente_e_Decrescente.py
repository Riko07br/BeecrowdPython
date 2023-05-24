while True:
    recebe = input().split(" ")
    n1, n2 = [int(i) for i in recebe]

    if n1 == n2:
        break

    print("Crescente" if n1 < n2 else "Decrescente")