import random

from django.test import TestCase

from .models import User, Stack


class StackModelTests(TestCase):

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

        self.stacks = [
            {
                "name": "Sharestack",
                "description": "The best stack centralized place",
                "private": False,
                "sharelink": "http://sharestack.org/s/213123123",
            },
            {
                "name": "Twitter",
                "description": "Twits, twits everywhere",
                "private": False,
                "sharelink": "http://sharestack.org/s/87654fedfd",
            },
            {
                "name": "Github",
                "description": "Share your code",
                "private": False,
                "sharelink": "http://sharestack.org/s/54fsfd12dassdf",
            },
            {
                "name": "SomePrivateApp",
                "description": "Something private",
                "private": True,
                "sharelink": "http://sharestack.org/s/fvdsqw12",
            }
        ]

        # Save user for the tests
        self.user_instances = []
        for i in self.users:
            u = User(**i)
            u.save()

            self.user_instances.append(u)

    def test_save(self):
        for i in self.stacks:
            s = Stack(**i)
            s.owner = self.user_instances[random.randrange(
                                            len(self.user_instances))]
            s.save()

        self.assertEqual(len(Stack.objects.all()), len(self.stacks))

    def test_retrieval(self):
        for i in self.stacks:
            s = Stack(**i)
            s.owner = self.user_instances[random.randrange(
                                            len(self.user_instances))]
            s.save() # First save before adding many to many fields
            s.collaborators.add(*self.user_instances)

            s2 = Stack.objects.get(id=s.id)
            self.assertEqual(s, s2)

    def test_filter(self):
        for i in self.stacks:
            s = Stack(**i)
            s.owner = self.user_instances[random.randrange(
                                            len(self.user_instances))]
            s.save()

        stack = self.stacks[random.randrange(len(self.stacks))]
        s = Stack.objects.filter(name=stack["name"])[0]
        self.assertEqual(s.description, stack["description"])

    def test_related_fields(self):
        for i in self.stacks:
            s = Stack(**i)
            s.owner = self.user_instances[0]
            s.save() # First save before adding many to many fields
            s.collaborators.add(*self.user_instances)

        # Check if user 0 is the owner of all the stacks
        u = User.objects.get(id=self.user_instances[0].id)
        self.assertEqual(len(u.owned_stack.all()), len(self.stacks))

        # Check if each users is as collaborator in all the instances
        for i in self.user_instances:
            u = User.objects.get(id=i.id)

    def test_str(self):
        for i in self.stacks:
            s = Stack(**i)
            self.assertEqual(str(s), i["name"])

            
            





