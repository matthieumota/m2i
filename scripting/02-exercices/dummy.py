import os
import random
import shutil

folders = ['A', 'B']

for folder in folders:
    shutil.rmtree(folder)
    os.makedirs(folder)

    for i in range(random.randint(5, 10)):
        file_ext = random.choice(['log', 'txt'])
        file_path = os.path.join(folder, f'log_{i+1}.{file_ext}')
        size = random.randint(0, 6 * 1024)
        with open(file_path, 'wb') as f:
            f.write(os.urandom(size))
        # if random.random() < 0.5:
            # os.chmod(file_path, 0o300)

print('Dossiers et fichiers générés.')
