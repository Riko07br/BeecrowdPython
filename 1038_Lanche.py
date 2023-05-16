order = input().split(" ")

orderInt = [int(numeric_string) for numeric_string in order]

prices = [4.0, 4.5, 5.0, 2.0, 1.5]

orderInt[0] -= 1

print("Total: R$ {:.2f}".format(prices[orderInt[0]] * orderInt[1]))