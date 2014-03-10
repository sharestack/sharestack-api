import random

from django.test import TestCase

from .models import User, Company


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


class CompanyModelTests(TestCase):

    def setUp(self):
        self.companies = [
            {
                "name": "DC",
                "url": "DCcomics.com",
                "description": """DC Comics, Inc. is one of the largest 
                    and most successful companies operating 
                    in the market for American comic books 
                    and related media""",
                "logo": "http://www.dccomics.com/logo.png",
            },
            {
               "name": "Marvel",
                "url": "marvel.com",
                "description": """is an American publisher 
                    of comic books and related media""",
                "logo": "http://www.marvel.com/logo.png",
            },
            {
                "name": "Darkhorse",
                "url": "darkhorse.com",
                "description": """Dark Horse Comics is an 
                    American comic book and manga publisher.""",
                "logo": "http://www.darkhorse.com/logo.png",
            },
        ]

    def test_save(self):
        for i in self.companies:
            company = Company(**i)
            company.save()

        self.assertEqual(len(Company.objects.all()), len(self.companies))

    def test_retrieval(self):
        for i in self.companies:
            company = Company(**i)
            company.save()
            company2 = Company.objects.get(id=company.id)
            self.assertEqual(company, company2)

    def test_filter(self):
        for i in self.companies:
            company = Company(**i)
            company.save()

        c = self.companies[random.randrange(len(self.companies))]
        company = Company.objects.filter(name=c["name"])[0]
        self.assertEqual(company.url, c["url"])

    def test_like(self):
        for i in self.companies:
            company = Company(**i)
            company.save()

        companies = Company.objects.filter(logo__contains='logo.png')
        self.assertEqual(len(companies), len(self.companies))

    def test_str(self):
        for i in self.companies:
            company = Company(**i)
            self.assertEqual(str(company), i["name"])


