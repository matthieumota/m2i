import psutil, subprocess

# Coeurs CPU
print('Coeurs CPU:', psutil.cpu_count())

# Utilisation du CPU
cpu_percent = psutil.cpu_percent(interval=1)
print(f'Utilisation CPU: {cpu_percent}%')

# Utilisation du CPU par coeurs
cpu_per_core = psutil.cpu_percent(interval=1, percpu=True)
for i, percent in enumerate(cpu_per_core):
    print(f'Core {i}: {percent}%')

# RAM
ram = psutil.virtual_memory()
print(f'Total RAM : {ram.total / (1024**3):.2f} GB')
print(f'RAM utilisée : {ram.used / (1024**3):.2f} GB')
print(f'RAM disponible : {ram.available / (1024**3):.2f} GB')
print(f'Utilisation RAM : {ram.percent}%')

# Utilisation du disque
usage = psutil.disk_usage('/')
print(f"Total: {usage.total / (1024**3):.2f} GB")
print(f"Utilisé : {usage.used / (1024**3):.2f} GB")
print(f"Disponible : {usage.free / (1024**3):.2f} GB")
print(f"Utilisation : {usage.percent}%")

# J'affiche les 10 premiers services
print('Services:')
result = subprocess.run(['launchctl', 'list'], capture_output=True, text=True)
print(result.stdout.splitlines()[:11])
print('\n'.join(result.stdout.splitlines()[:11])) # Affiche les 10 premières lignes

from tqdm import tqdm
import time

with tqdm(total=100) as cpubar:
    while True:
        cpubar.n = psutil.cpu_percent()
        cpubar.refresh()
        time.sleep(0.5)
