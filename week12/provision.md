## Pre install some dependencies:
```
sudo apt-get install python-virtualenv
```

## nginx:

Install nginx:

```
sudo apt-get install nginx
sudo service nginx start
```

## Install postgresql

```
sudo apt-get install postgresql postgresql-server-dev-9.3
sudo pg_createcluster 9.3 main
sudo service postgresql start
```
If `pg_createcluster` fails do the following:

```
export LC_ALL="en_US.UTF-8"
```

## Create `user` that will execute the python code

```
adduser hack
```

## Create folder for the project & virtual environment

```
mkdir hack
chown hack:hack -R hack/ # Give ownership to the hack user
```

**Important** Do everything esle as the hack user

```
su hack
cd /hack
mkdir <project_dir>
cd <project_dir>
virtualenv -p /usr/bin/python3 env
source env/bin/activate
mkdir current
cd current
git clone <git_repo_here>.
pip install -r requirements.tt
```

## Set env variables

```
vi /etc/environment  # Paste your environments here
```

## Create postgres user & db

**Important note** Run the next commands as root

```
sudo -u postgres createuser hack
sudo -u postgres createdb -O hack hack33
```

**Important note** ssh again as hack so that env variables are recongnized!

## Run migrations

```
python manage.py migrate
```

### check your work

```
python manage.py runserver 0.0.0.0:8000
```

## Setup gunicorn

**Important note** You won't be able to access it from outside

```
gunicorn config.wsgi:application
```

## Setup upstart job that's gona keep the gunicorn up

**Important note** Execute the next commands as `root`

Check the [upstart conf.](config/upstart.conf)
```
cd /etc/init/
vi <project_name>.conf
start <project_name>
```

## Setup nginx

**Important note** Run the following commands as `root`

Check the [nginx conf.](config/nginx.conf)


```
cd /etc/nginx/sites-enabled
rm default
vi <project_name> # paste the nginx config from this repo
sudo service nginx restart
```