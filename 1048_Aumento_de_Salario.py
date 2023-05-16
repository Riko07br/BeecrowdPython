salary = float(input())

percent = .04

if salary <= 400.00:
    percent = .15
elif salary <= 800.00:
    percent = .12
elif salary <= 1200.00:
    percent = .1
elif salary <= 2000.00:
    percent = .07

print("Novo salario: {:.2f}".format(salary * (1 + percent)))
print("Reajuste ganho: {:.2f}".format(salary * percent))
print("Em percentual: {:.0f} %".format(percent * 100))