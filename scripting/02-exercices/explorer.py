from datetime import datetime
import humanize
import os
import pathlib
import subprocess
import zipfile

folder = input('Quel dossier voulez-vous explorer/nettoyer ? (Vide pour le dossier courant): ')

if not folder:
    folder = os.getcwd()

path = pathlib.Path(folder)

if not path.exists():
    print(f'Le dossier "{folder}" n\'existe pas.')
    exit(1)

files = list(path.glob('*.log'))

if not files:
    print('Aucun fichier .log trouvé.')
    exit(1)

to_archive = []

print('🔍 Fichiers .log trouvés :')

for file in files:
    size_bytes = file.stat().st_size
    size = humanize.naturalsize(size_bytes)
    time = datetime.fromtimestamp(file.stat().st_mtime).strftime('%d/%m/%Y %H:%M')

    readable = 'OK' if os.access(file, os.R_OK) else '❌'
    writable = 'OK' if os.access(file, os.W_OK) else '❌'

    print(f'- {file.name} ({size}, modifié le {time})')

    if size_bytes > 5 * 1024:
        os.remove(file)
        print(f'⚠️ Supprimé (trop gros)')
    else:
        if os.access(file, os.R_OK):
            to_archive.append(file)

        print(f'  ↪️ Lecture : {readable} | Écriture : {writable}')

if to_archive:
    archive_path = os.path.join(path, 'logs_archive.zip')
    with zipfile.ZipFile(archive_path, 'w') as zipf:
        for f in to_archive:
            zipf.write(f)
    print(f'\n📦 Archive créée : logs_archive.zip')
else:
    print('\n📦 Aucun fichier à archiver.')

print('\n📁 Résultat de ls -lh :')
result = subprocess.run(['ls', '-lh', folder], capture_output=True, text=True)
print(result.stdout)
