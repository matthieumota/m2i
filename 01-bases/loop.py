print([*range(0)])
print([*range(2, 10, 1)])
print([0, 1, 2, 3, 4])

for i in [1, 2, 3]:
    print(i)

for i in range(1, 4):
    print(i)

cars = ['ferrari', 'porsche', 'bmw']
for car in cars:
    print(car)

numberA = input('Saisis un nombre entre 1 et 18: ')

while not numberA.isnumeric() or int(numberA) < 1 or int(numberA) > 18:
    numberA = input('Saisis un nombre entre 1 et 18: ')

for i in range(1, int(numberA) + 1):
    print(i)

count = 0

while count < 10:
    print(count)
    count += 1

for i in range(10):
    if i % 2 == 1:
        continue
    if i == 6:
        break
    print(i)
