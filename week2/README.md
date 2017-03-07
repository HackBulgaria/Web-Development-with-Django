# Week 2

## Agenda for the first week. 
- Setup a PostgreSQL Server
- Connect django project to the PostgreSQL server
- Models
- Migrations

## Setting up PostgreSQL

Install the PostgreSQL server:
```
$ sudo apt-get install postgresql postgresql-contrib
```

Switch over to the postgres account on your server by typing:

```
$ sudo -i -u postgres
```

You can now access a Postgres prompt immediately by typing:
```
$ psql
```

First, we will create a database for our Django project. Each project should have its own isolated database for security reasons. 
```sql
CREATE DATABASE myproject;
```

Next, we will create a database user which we will use to connect to and interact with the database.

```sql
CREATE USER myprojectuser WITH PASSWORD 'password';
```

Now, all we need to do is give our database user access rights to the database we created:
```sql
GRANT ALL PRIVILEGES ON DATABASE myproject TO myprojectuser;
```

## Connect django to PostgreSQL

Install python`s adapter for PostgreSQL. [psycopg2](http://initd.org/psycopg/docs/usage.html)
```
$ pip install psycopg2
```

Connect your django app with the PostgreSQL server.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'myproject',
        'USER': 'myprojectuser',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```


Docs for further reading:

* <https://docs.djangoproject.com/en/1.10/topics/db/models/>
* <https://docs.djangoproject.com/en/1.10/topics/db/queries/>
