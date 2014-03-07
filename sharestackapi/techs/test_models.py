import random

from django.test import TestCase

from .models import TechType


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
