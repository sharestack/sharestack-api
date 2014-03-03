import random

from django.test import TestCase

from .models import User


class UserModelTests(TestCase):

    def setUp(self):
        self.users = [
            {
                "username": "batman",
                "first_name": "Bruce",
                "last_name": "Wayne",
                "email": "thedarkknight@superheroes.com",
                "password": "GothamCityWillBeSafe",
                "url": "http://imbatman.com",
                "gravatar": "thedarkknight@superheroes.com",
            },
            {
                "username": "spiderman",
                "first_name": "Peter",
                "last_name": "Parker",
                "email": "spiderwebmaster@superheroes.com",
                "password": "ILoveYouMJ",
                "url": "iloveradiactivespiders.com",
                "gravatar": "spiderwebmaster@superheroes.com",
            },
            {
                "username": "wolveryne",
                "first_name": "Logan",
                "last_name": "",
                "email": "clawpowerX@superheroes.com",
                "password": "kissMyClaws",
                "url": "wolvesandmutants.com",
                "gravatar": "clawpowerX@superheroes.com",
            },
        ]

    def test_save(self):
        for i in self.users:
            u = User(**i)
            u.save()

        self.assertEqual(len(User.objects.all()), len(self.users))

    def test_retrieval(self):
        for i in self.users:
            u = User(**i)
            u.save()
            u2 = User.objects.get(id=u.id)
            self.assertEqual(u, u2)

    def test_filter(self):
        for i in self.users:
            u = User(**i)
            u.save()

        user = self.users[random.randrange(len(self.users))]
        u = User.objects.filter(username=user["username"])[0]
        self.assertEqual(u.email, user["email"])

    def test_like(self):
        for i in self.users:
            u = User(**i)
            u.save()

        users = User.objects.filter(email__contains='superheroes.com')
        self.assertEqual(len(users), len(self.users))

    def test_str(self):
        for i in self.users:
            u = User(**i)
            self.assertEqual(str(u), i["username"])


