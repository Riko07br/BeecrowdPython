order = input().split(" ")

cod, quant = [int(n) for n in order]
cod -=1

prices = [4.0, 4.5, 5.0, 2.0, 1.5]

print("Total: R$ {:.2f}".format(prices[cod] * quant))