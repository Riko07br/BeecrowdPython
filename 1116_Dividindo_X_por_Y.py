loops = int(input())

for i in range(loops):
    x, y = [int(i) for i in input().split(" ")]

    if y == 0:
        print("divisao impossivel")
        continue

    print(f"{x/y:.1f}")