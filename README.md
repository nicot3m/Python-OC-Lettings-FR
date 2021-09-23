## Résumé

Site web d'Orange County Lettings

![logo OC lettings](logo_OC_lettings.png) 

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).
- Pour arrêter le serveur, `Ctrl + Pause`

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(oc_lettings_site_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from oc_lettings_site_profile where favorite_city like 'B%';`
- NB initially `Python-OC-Lettings-FR_profile` replaced by `oc_lettings_site_profile`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :
- Pour changer le Set-ExecutionPolicy de windows (à faire une fois), `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Pour sortir de l'environnement virtuel, `deactivate`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


### Variables d'environnement en local
- **Attention**, pour tester le site refactorisé en local, il est conseillé d'ajouter à la racine du projet le fichier .env
- Il n'est pas sous GiHhub pour des raisons de sécurité
- .env contient les variables:
	- DJANGO_SECRET_KEY
	- DSN_SENTRY
	- DEBUG_VALUE


## Déploiement

### Workflow CircleCI

Déploiement automatique à l'aide du pipeline CircleCI à chaque push du projet dans GitHub en suivant le wokflow suivant:
1. Récupération du code (checkout)
2. Installation des packages listés dans requirements.txt avec pip
3. Lancement des tests avec pytest
4. Vérification du linting avec flake8
5. Création du container avec l'image du projet dans le dépôt DockerHub
6. Déploiement web sous Heroku
7. Suivi des erreurs et des performances avec Sentry

Remarques:
- Les étapes 1 à 4 sont lancées par un push sur n'importe quelle branche
- Un succès aux étapes 1 à 4 est un pré-requis à l'étape 5
- Un succès à l'étape 5 est un pré-requis à l'étape 6
- Les étapes 5 à 7 ne sont lancés qu'avec un push de la branche master


### Configuration requise

Les comptes suivants sont nécessaires:
- GitHub
- CircleCI
- DockerHub
- Heroku
- Sentry

Il est utile d'installer en local les programmes suivants:
- Docker Desktop or Docker Engine for Linux
- HerokuCLI


### Guide de déploiement

#### Étape1: DockerHub

- Se connecter à Docker
- Créer un dépôt (Create Repository)
- Renseigner le nom du dépôt: oc_lettings_site_build


#### Étape2: Heroku

- Se connecter à Heroku
- Cliquer sur New\Create new app
- Renseigner le nom de l'application: oc-lettings-2021

Remarque:
Peut aussi se faire depuis le terminal avec la commande `heroku create oc-lettings-2021`


#### Étape3: Sentry

- Se connecter à Sentry
- Menu Projects\Create Project
- Choisir la plateforme: django
- Renseigner le nom du projet: oc_lettings_site


#### Étape4: CircleCI

- Se connecter à CircleCI avec son compte GitHub
- Menu Projects: rechercher le projet Python-OC-Lettings-FR
- Set Up Poject: choisir "if you already have.circleci/config.yml" et branche master
- Project Settings\Environment Variables\Add Environment Variable

|Name|Description|Note|
|:---- |:-------|:-----:|
|DJANGO_SECRET_KEY|Clé secrête Django|Note 1|
|DOCKER_LOGIN|Votre identifiant DockerHub| |
|DOCKER_PASSWORD|Votre mot de passe ou token DockerHub |Note 2|
|DSN_SENTRY|Votre clé client Sentry|Note 3|
|HEROKU_API_KEY|Le token Heroku|Note 4|
|HEROKU_APP_NAME|Le nom de votre appli sous Heroku|Note 5|
|PROJECT_REPONAME|Le nom du dépôt dans DockerHub|Note 6|
|DEBUG_VALUE|Debug mode de Django|Note 7|

Note:
1. Pour générer une nouvelle clé secrête Django: `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
2. Pour générer un nouveau token DockerHub: Account Settings\Security\New Access Token
3. Pour récupérer votre clé client Sentry: Sentry\project\roue dentée pour settings\Client Keys (DSN)
4. Pour créer un long-term token heroku en production: `heroku authorizations:create -j`
5. Pour ce projet, le nom oc-lettings-2021 a été choisi
6. Pour ce projet, le nom oc_lettings_site_build a été choisi
7. True en développement et False en production

#### Étape5: Récupérer l'image sur DockerHub et lancer le site en local

- Ouvrir Docker Desktop
- Récupérer l'image en local: `docker pull your_docker_login/oc_lettings_site_build:tag`
- Tag is found in DockerHub
- Lister les images: `docker images`
- Lancer le container Docker avec le fichier des variables d'environnement locales: `docker run --env-file .env  -d -p 8000:8000 your_docker_login/oc_lettings_site_build:tag`
- Tester le site dans votre navigateur: `http://127.0.0.1:8000/`
- Lister les container Docker lancés: `docker container ps`
- Arrêter le container: `docker stop CONTAINER ID`
- Nettoyer: `docker system prune`
