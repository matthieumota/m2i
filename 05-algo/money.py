try:
    amount = int(input('Quelle est la somme ? '))
except ValueError:
    print('Veuillez entrer un nombre entier')
    exit()

bills = [50, 20, 10, 5, 2, 1]

for bill in bills:
    if amount >= bill:
        rest = amount % bill # 68 % 50 = 18
        count = round((amount - rest) / bill) # 50 / 50 = 1
        print(count, 'x', bill, '€')
        amount -= count * bill
