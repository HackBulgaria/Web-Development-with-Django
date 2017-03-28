# Queries over Loki

Your task is to setup [Loki](https://github.com/HackSoftware/Loki), write a management command and do some queries.

## Management command - seed database

We want to write a [custom management command](https://docs.djangoproject.com/en/1.10/howto/custom-management-commands/) that will create some fake data for us:

```bash
$ python manage.py seed_database
```

Use the existing [factories](https://github.com/HackSoftware/Loki/blob/master/loki/seed/factories.py) and faker to achieve that.

We want to seed the database with:

* 5 courses
* 20 students for each course
* 1 teacher for each of the courses
* 2 week content for each course - lectures, materials, problems
* Solutions from all students for all problems

## Queries

Now, in a Django shell, we want to make queries for:

* List all courses
* List all students
* List all students for a given course 
* List all materials for a given course
* Count the number of solutions for a given course
* Count the number of solutions for a given task, for a given course
