import random

from django.test import TestCase

from members.models import User
from techs.models import Tech, Component
from .models import Stack, Instance


# shared data across the tests
users = [
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

stacks = [
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

instances = [
    {
        "name": "erebor",
        "ram": "1.7GiB",
        "cpu": "1(ECU), 1(vCPU)",
        "hdd": "1x160GiB",
        "instance_type": "m1.small",
        "provider": "Amazon AWS",
        "provider_name": "Amazon Linux AMI 2013.09.2 - ami-ccf297fc (64-bit)",
        "description": "Small"
    },
    {
        "name": "rohan",
        "ram": "3.75GiB",
        "cpu": "6.5(ECU), 2(vCPU)",
        "hdd": "1x4GiB (SSD)",
        "instance_type": "m3.medium",
        "provider": "Amazon AWS",
        "provider_name": "Red Hat Enterprise Linux 6.4 (PV) - ami-b8a63b88",
        "description": "Medium"
    },
    {
        "name": "the-shire",
        "ram": "68.4GiB",
        "cpu": "26(ECU), 8(vCPU)",
        "hdd": "2x840GiB",
        "instance_type": "m2.4xlarge",
        "provider": "Amazon AWS",
        "provider_name": "Ubuntu Server 12.04 LTS (PV) - ami-fa9cf1ca (64-bit)",
        "description": "Big"
    },
    {
        "name": "mordor",
        "ram": "60.5GiB",
        "cpu": "35(ECU), 16(vCPU)",
        "hdd": "2x1024GiB (SSD)",
        "instance_type": "hi1.4xlarge",
        "provider": "Amazon AWS",
        "provider_name": "Ubuntu Server 13.10 (PV) - ami-7eaecc4e (64-bit)",
        "description": "Gigantic"
    },
    {
        "name": "gondor",
        "ram": "30GiB",
        "cpu": "55(ECU), 16(vCPU)",
        "hdd": "2x160GiB (SSD)",
        "instance_type": "c3.4xlarge",
        "provider": "Amazon AWS",
        "provider_name": "SuSE Linux Enterprise Server 11 sp3 (HVM) ",
        "description": "Badass"
    },
]

techs = {
    "postgresql": {
        "name": "postgresql",
        "description": "The best relational database",
        "url": "http://www.postgresql.org/",
        "logo": "http://someimage.com/some.png",
        "open_source": True,
        "repo": "https://github.com/postgres/postgres",
    },
    "nginx": {
        "name": "nginx",
        "description": "The best http server",
        "url": "http://nginx.org/",
        "logo": "http://someimage.com/some.png",
        "open_source": True,
        "repo": "http://hg.nginx.org/nginx",
    },
}

components = {
    "nginx": {
        "name": "nginx",
        "version": "1.5.11",
        "config": 'nginx config big string',
        "description": "This is a description of a versioned nginx",
    },
    "postgresql": {
        "name": "postgresql",
        "version": "9.3",
        "config": 'postgres config',
        "description": "This is a description of a versioned postgres",
    },
}


class StackModelTests(TestCase):

    def setUp(self):
        # Save user for the tests
        self.user_instances = []
        for i in users:
            u = User(**i)
            u.save()

            self.user_instances.append(u)

    def test_save(self):
        for i in stacks:
            s = Stack(**i)
            s.owner = self.user_instances[random.randrange(
                                            len(self.user_instances))]
            s.save()

        self.assertEqual(len(Stack.objects.all()), len(stacks))

    def test_retrieval(self):
        for i in stacks:
            s = Stack(**i)
            s.owner = self.user_instances[random.randrange(
                                            len(self.user_instances))]
            s.save() # First save before adding many to many fields
            s.collaborators.add(*self.user_instances)

            s2 = Stack.objects.get(id=s.id)
            self.assertEqual(s, s2)

    def test_filter(self):
        for i in stacks:
            s = Stack(**i)
            s.owner = self.user_instances[random.randrange(
                                            len(self.user_instances))]
            s.save()

        stack = stacks[random.randrange(len(stacks))]
        s = Stack.objects.filter(name=stack["name"])[0]
        self.assertEqual(s.description, stack["description"])

    def test_related_fields(self):
        for i in stacks:
            s = Stack(**i)
            s.owner = self.user_instances[0]
            s.save() # First save before adding many to many fields
            s.collaborators.add(*self.user_instances)

        # Check if user 0 is the owner of all the stacks
        u = User.objects.get(id=self.user_instances[0].id)
        self.assertEqual(len(u.owned_stack.all()), len(stacks))

        # Check if each users is as collaborator in all the instances
        for i in self.user_instances:
            u = User.objects.get(id=i.id)
            self.assertEqual(len(u.collaboration_stack.all()), len(stacks))


    def test_str(self):
        for i in stacks:
            s = Stack(**i)
            self.assertEqual(str(s), i["name"])

                        
class InstanceModelTests(TestCase):

    def setUp(self):
        
        self.users = []
        self.stacks = []
        
        # Save user for the tests
        for i in users:
            u = User(**i)
            u.save()

            self.users.append(u)

        for i in stacks:
            s = Stack(**i)
            s.owner = self.users[0] # Batman always owner
            s.save()
            self.stacks.append(s)


    def test_save(self):
        for i in instances:
            it = Instance(**i)
            it.stack = self.stacks[random.randrange(len(self.stacks))]
            it.save()

        self.assertEqual(len(Instance.objects.all()), len(instances))

    def test_retrieval(self):
        for i in instances:
            it = Instance(**i)
            it.stack = self.stacks[random.randrange(len(self.stacks))]
            it.save()

            it2 = Instance.objects.get(id=it.id)
            self.assertEqual(it, it2)

    def test_filter(self):
        selected_stacks = {}
        for i in instances:
            it = Instance(**i)

            selected_stacks[it.name] = \
                            self.stacks[random.randrange(len(self.stacks))]

            it.stack = selected_stacks[it.name]
            it.save()

        instance = instances[random.randrange(len(instances))]
        it = Instance.objects.filter(name=instance["name"])[0]
        self.assertEqual(it.stack, selected_stacks[it.name])

    def test_related_fields(self):
        selected_stacks = {}
        for i in instances:
            it = Instance(**i)

            # first stack (Sharestack) has all the instances
            selected_stacks[it.name] = self.stacks[0]

            it.stack = selected_stacks[it.name]
            it.save()

        s = Stack.objects.get(name=self.stacks[0].name)
        self.assertEqual(len(s.instance_set.all()), len(instances))

        # check that component relation is ok
        nginx_tech = Tech(**techs["nginx"])
        nginx_tech.save()
        nginx = Component(**components["nginx"])
        nginx.tech = nginx_tech
        postgresql_tech = Tech(**techs["postgresql"])
        postgresql_tech.save()
        postgresql = Component(**components["postgresql"])
        postgresql.tech = postgresql_tech

        nginx.save()
        postgresql.save()

        it = Instance.objects.get(name="erebor")
        it2 = Instance.objects.get(name="rohan")
        it.components.add(nginx, postgresql)
        it2.components.add(nginx)

        nginx2 = Component.objects.get(name="nginx")
        postgresql2 = Component.objects.get(name="postgresql")

        self.assertEqual(len(nginx2.instance_set.all()), 2)
        self.assertEqual(len(postgresql2.instance_set.all()), 1)

    def test_str(self):
        for i in instances:
            it = Instance(**i)
            self.assertEqual(str(it), i["name"])
