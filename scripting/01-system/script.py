import os

print(os.getcwd())
print(os.listdir('.'))

if os.path.exists('titi.txt'):
    os.rename('titi.txt', 'tutu.txt')
else:
    os.rename('tutu.txt', 'titi.txt')

if os.path.isfile('toto.txt'):
    os.remove('toto.txt')

print(os.access('script.py', os.R_OK))
os.chmod('test', 0o400)
print(os.access('test', os.W_OK))

print(os.path.basename('/aaa/bbb/test'))
print(os.path.dirname('/aaa/bbb/test'))
print(os.path.isdir('.venv'))
print(os.path.isfile('.venv'))
print(os.path.getsize('script.py'))

# print(os.getuid()) # id utilisateur (0 root)
import sys
print(sys.platform) # win32, linux, darwin

import platform
print(platform.architecture())
print(platform.mac_ver())
print(platform.win32_ver())

print(os.path.abspath('script.py'))
print(os.path.join('a', 'b', 'test')) # a/b/test

from pathlib import Path

p = Path('.')
print([*p.iterdir()])
for f in p.iterdir():
    print(f.name, f.stat().st_size)

import shutil

os.remove('test2')
shutil.copy('test', 'test2')
shutil.rmtree('titi')
shutil.copytree('toto', 'titi')

shutil.make_archive('archive', 'zip', '.')
print(shutil.disk_usage('/'))
du = shutil.disk_usage('/')
print(du.total / 1024 / 1024 / 1024)

import glob

print('------')

for f in glob.glob('*.txt'):
    print(f, os.path.getsize(f))

import subprocess

result = subprocess.run(['ls', '-l', '.venv'], capture_output=True)
if result.returncode != 0:
    print('Bon ton dossier il existe pas là')
else:
    print(result.stdout)

import shlex
ask = input('Tape un dossier où tu veux ls')
subprocess.run(f'ls -l {shlex.quote(ask)}', shell=True)
