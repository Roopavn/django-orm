# django-orm

What is orm?
ORM is an acronym for the object-relational mapper. The ORM’s main goal is to transmit data between a relational database and application model. The ORM automates this transmission, such that the developer need not write any SQL.

ORM, as from the name, maps objects attributes to respective table fields. It can also retrieve data in that manner.

Is it necessary to use ORM?
This is totally a developer’s choice. Although there are certain benefits of ORM, there are some downsides too. It is beneficial for developers as it allows faster development. Sometimes ORMs generate more complex queries then they should. This can result in a performance decrease. Therefore, it is totally the developer’s choice and the level of work they are doing. For example – Django ORM is efficient for working with low-medium complexity models.


What is a QuerySet?
We all use queries to retrieve data from the database. Querysets are Django’s way to retrieve data from the database. The Django ORM lets us use Querysets.

A Queryset is a list of objects of a model. We use Querysets to filter and arrange our data. These make our work as a Python developer easier.
A QuerySet is, in essence, a list of objects of a given Model. QuerySets allow you to read the data from the database, filter it and order it.

It's easiest to learn by example. Let's try this, shall we?


