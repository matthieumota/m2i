import os
currentpath = os.getcwd()

with open(f'{currentpath}/file.txt','a+',encoding='utf8') as file:
    file.seek(0)
    for number in range(0,11,2):
        # if number % 2 == 0:
        file.seek(0)
        line = file.readline(1).strip()
        if int(line) == number:
            print(f'Le nombre {number} est bien écrit dans le fichier')
        else:
            file.write(f'{number}\n')
            print(f'Le nombre {number} n\'est pas bien écrit dans le fichier')
 