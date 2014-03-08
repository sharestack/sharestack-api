import random

from django.test import TestCase

from .models import TechType, Tech


# shared data across the tests
types = [
    {
        "name": "framework",
        "description": "to do web stuff"
    },
    {
        "name": "database",
        "description": "to store stuff"
    },
    {
        "name": "application",
        "description": "to show stuff"
    },
    {
        "name": "balancer",
        "description": "to balance stuff"
    },
    {
        "name": "web server",
        "description": "to serve stuff"
    },
    {
        "name": "programming language",
        "description": "to programm stuff"
    },
]

techs = [
    {
        "name": "django",
        "description": "The best web framework",
        "url": "https://www.djangoproject.com/",
        "logo": "http://someimage.com/some.png",
        "open_source": True,
        "repo": "https://github.com/django/django.git",
    },
    {
        "name": "python",
        "description": "The programming language",
        "url": "http://www.python.org/",
        "logo": "http://someimage.com/some.png",
        "open_source": True,
        "repo": "http://hg.python.org/cpython/",
    },
    {
        "name": "golang",
        "description": "The other programming language",
        "url": "http://www.golang.org/",
        "logo": "http://someimage.com/some.png",
        "open_source": True,
        "repo": "https://code.google.com/p/go",
    },
    {
        "name": "postgresql",
        "description": "The best relational database",
        "url": "http://www.postgresql.org/",
        "logo": "http://someimage.com/some.png",
        "open_source": True,
        "repo": "https://github.com/postgres/postgres",
    },
    {
        "name": "nginx",
        "description": "The best http server",
        "url": "http://nginx.org/",
        "logo": "http://someimage.com/some.png",
        "open_source": True,
        "repo": "http://hg.nginx.org/nginx",
    },
    {
        "name": "sharestack",
        "description": "The best app",
        "url": "http://sharestack.org/",
        "logo": "http://someimage.com/some.png",
        "open_source": True,
        "repo": "https://github.com/sharestack/sharestack",
    },
]


class TechTypeTests(TestCase):

    def setUp(self):
        pass

    def test_save(self):
        for i in types:
            t = TechType(**i)
            t.save()

        self.assertEqual(len(TechType.objects.all()), len(types))

    def test_retrieval(self):
        for i in types:
            t = TechType(**i)
            t.save()

            t2 = TechType.objects.get(id=t.id)
            self.assertEqual(t, t2)

    def test_filter(self):
        for i in types:
            t = TechType(**i)
            t.save()

        tech_type = types[random.randrange(len(types))]
        t = TechType.objects.filter(name=tech_type["name"])[0]
        self.assertEqual(t.description, tech_type["description"])

    def test_str(self):
        for i in types:
            t = TechType(**i)
            self.assertEqual(str(t), i["name"])


class TechTests(TestCase):

    def setUp(self):
        # Save first all the types
        self.type_objects = {}
        for i in types:
            t = TechType(**i)
            t.save
            self.type_objects[i["name"]] = t

    def test_save(self):
        for i in techs:
            t = Tech(**i)
            t.save()

        self.assertEqual(len(Tech.objects.all()), len(techs))

    def test_retrieval(self):
        for i in techs:
            t = Tech(**i)
            t.save()

            t2 = Tech.objects.get(id=t.id)
            self.assertEqual(t, t2)

    def test_filter(self):
        for i in techs:
            t = Tech(**i)
            t.save()

        tech = techs[random.randrange(len(techs))]
        t = Tech.objects.filter(name=tech["name"])[0]
        self.assertEqual(t.url, tech["url"])

    def test_related_fields(self):
        # Create types
        programming_lang = TechType(**types[5])  # Is the 6th
        app = TechType(**types[2])  # Is the 3rd
        framework = TechType(**types[0])  # Is the 1st
        database = TechType(**types[1])  # Is the 2nd

        # Create techs
        python = Tech(**techs[1])  # Is the 2nd
        go = Tech(**techs[2])  # Is the 3rd
        django = Tech(**techs[0])  # Is the 1st
        sharestack = Tech(**techs[-1])  # Is the last
        postgres = Tech(**techs[3])  # Is the 4th

        # Save before adding m2m fields
        programming_lang.save()
        app.save()
        framework.save()
        database.save()

        # save remaining
        python.save()
        go.save()
        django.save()
        sharestack.save()
        postgres.save()

        # add types
        python.types.add(programming_lang)
        go.types.add(programming_lang)
        django.types.add(framework)
        sharestack.types.add(app)
        postgres.types.add(database)

        # Check types are ok in both sides for programmign languages
        python2 = Tech.objects.get(name=python.name)
        go2 = Tech.objects.get(name=go.name)
        programming_lang2 = TechType.objects.get(name=programming_lang.name)

        self.assertEqual(python2.types.all()[0], programming_lang2)
        self.assertEqual(go2.types.all()[0], programming_lang2)
        self.assertEqual(len(programming_lang2.tech_set.all()), 2)

        # Check tech componente are ok in one side with sharestack
        django.tech_components.add(python)
        sharestack.tech_components.add(python, django, postgres)

        self.assertEqual(len(sharestack.tech_components.all()), 3)

        # Isn't symmetrical so postgres shouldn't have sharestack
        self.assertEqual(len(postgres.tech_components.all()), 0)

    def test_str(self):
        for i in techs:
            t = Tech(**i)
            self.assertEqual(str(t), i["name"])
