# ndi-2021


# Activiation du venv
## Si dossier venv pas encore créé :
```bash
python3 -m venv venv
```
(ou python si votre python3 est python)\
ou\
```
virtualenv -p python3 venv
```

## Activation du venv
### Linux:
```bash
source venv/bin/activate
```
### Windows:
```cmd
cd venv/Scripts
activate.bat
cd ../..
```

# Installation des dependances :
```bash
pip3 install -r requirements.txt
```

# Lancer:
## Linux :
### Créer la database
``̀ 
FLASK_APP="app" DATABASE_URL="sqlite:///db.db" flask db create
```

```
FLASK_APP="app" DATABASE_URL="sqlite:///db.db?check_same_thread=False" flask run
```