# TP Python DevSecOps

## Installation des dépendances :

On crée un environnement Python puis :

```bash
pip install -r requirements.txt
```

On a besoin de lancer l'api :

```bash
uvicorn fake_api:app --reload
```

On peut lancer le monitoring :

```bash
python monitor.py
```

On peut vérifier le code :

```bash
python check_code.py
```

On peut lancer une base de données avec Docker :

```bash
docker run -e MYSQL_ROOT_PASSWORD=root \
  -v "$PWD/setup.sql":/docker-entrypoint-initdb.d/setup.sql \
  -p 3306:3306 -d mysql:8
```
