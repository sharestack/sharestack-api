import sys
import random
from datetime import datetime
# Check which version
import sys
if sys.hexversion < 0x03000000:  # Python2 import
    from urlparse import urlparse
else:  # Python3 import
    from urllib.parse import urlparse

from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from members.models import User
from .models import Stack


class StackAPITests(APITestCase):

    def setUp(self):

        user_data = [
            {
                "username": "profesor-X",
                "password": "I love my Xmen",
                "first_name": "Charles",
                "last_name": "Xavier",
                "is_superuser": True,
                "is_active": True,
                "is_staff": True,
            },
            {
                "username": "Batman",
                "password": "Dark_knight",
                "first_name": "Bruce",
                "last_name": "Wayne",
                "is_superuser": True,
                "is_active": True,
                "is_staff": True,
            },
            {
                "username": "Spiderman",
                "password": "The amazing one",
                "first_name": "Peter",
                "last_name": "Parker",
                "is_superuser": True,
                "is_active": True,
                "is_staff": True,
            }
        ]

        # The saved users, for using in the tests data
        self.users = []

        for i in user_data:
            u = User()
            for k, v in i.items():
                setattr(u, k, v)

            # Set the password correctly
            u.set_password(i["password"])
            u.save()
            self.users.append(u)

        # Login, we could use: 'force_authenticate' but we will login
        # as always, the 'classic' way, wiht DRF help
        self.client.login(username=u.username,
                          password=user_data[len(user_data)-1]["password"])

        self.data = {
            "name": "X-men stack",
            "description": "My amazing stack",
            "private": False,
            "sharelink": "http://dsads.com/adsad",
            "owner": reverse('user-detail', args=[self.users[0].id]),
            "collaborators": [
                reverse('user-detail', args=[self.users[1].id]),
                reverse('user-detail', args=[self.users[2].id]),
            ]
        }

    def test_create(self):
        url = reverse('stack-list')

        # Json default format in settings.py
        response = self.client.post(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Can't check as a full equals because id... are autofields
        for k, v in self.data.items():
            # don't check group lists
            if k not in ("collaborators", "owner"):
                self.assertEqual(response.data[k], self.data[k])

            self.assertEqual(urlparse(response.data["owner"]).path,
                             self.data["owner"])

            self.assertEqual(len(response.data["collaborators"]),
                             len(self.users[1:]))

    def test_update(self):
        # Save first (We have already, but we will get the id)
        url = reverse('stack-list')

        response = self.client.post(url, self.data)

        # Update later
        url = reverse('stack-detail', args=[response.data["id"]])

        self.data["name"] = "X-men stack2"
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Can't check as a full equals because id... are autofields
        for k, v in self.data.items():
            # don't check group lists
            if k not in ("collaborators", "owner"):
                self.assertEqual(response.data[k], self.data[k])

            self.assertEqual(urlparse(response.data["owner"]).path,
                             self.data["owner"])

            self.assertEqual(len(response.data["collaborators"]),
                             len(self.users[1:]))

    def test_detail(self):
        # Save first (We have already, but we will get the id)
        url = reverse('stack-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('stack-detail', args=[response.data["id"]])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Can't check as a full equals because id... are autofields
        for k, v in self.data.items():
            # don't check group lists
            if k not in ("collaborators", "owner"):
                self.assertEqual(response.data[k], self.data[k])

            self.assertEqual(urlparse(response.data["owner"]).path,
                             self.data["owner"])

            self.assertEqual(len(response.data["collaborators"]),
                             len(self.users[1:]))

    def test_delete(self):
         # Save first (We have already, but we will get the id)
        url = reverse('stack-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('stack-detail', args=[response.data["id"]])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list(self):
        url = reverse('stack-list')

        before = self.client.get(url).data["count"]

        # Sove N users
        number_users = random.randrange(20, 100)
        for i in range(number_users):
            self.data["name"] = "Stack-{0}".format(i)
            response = self.client.post(url, self.data)

        response = self.client.get(url)

        self.assertEqual(response.data["count"], number_users + before)
