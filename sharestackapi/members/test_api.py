import sys
import random
from datetime import datetime
# Check which version
import sys
if sys.hexversion < 0x03000000:  # Python2 import
    from urlparse import urlparse
else:  # Python3 import
    from urllib.parse import urlparse

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission, Group
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import User


class UserAPITests(APITestCase):

    def setUp(self):
        # Set an user so we can use the API
        password = "I love my Xmen"
        u = User()
        u.username = "profesor-X"
        u.set_password(password)
        u.first_name = "Charles"
        u.last_name = "Xavier"
        u.is_superuser = True
        u.is_active = True
        u.is_staff = True
        u.save()

        # Save content type
        c1 = ContentType(name="test1", app_label="test", model="test")
        c1.save()

        # Save 2 groups
        g1 = Group(name="test1")
        g2 = Group(name="test2")

        g1.save()
        g2.save()

        # Save 2 permissions
        p1 = Permission(name="test1", codename="test1", content_type=c1)
        p2 = Permission(name="test2", codename="test2", content_type=c1)

        p1.save()
        p2.save()

        # Login, we could use: 'force_authenticate' but we will login
        # as always, the 'classic' way, wiht DRF help
        self.client.login(username=u.username, password=password)

        self.data = {
            "username": "batman",
            "is_superuser": True,
            "password": u'pbkdf2_sha256$12000$r9vx2aWg13x218slB59DrbMWO8=...',
            "first_name": "Bruce",
            "last_name": "Wayne",
            "email": "thedarkknight@gmail.com",
            "is_staff": False,
            "is_active": True,
            "url": "http://jokeryouwillbebeaten.org",
            "gravatar": "thedarkknight@gmail.com",
            "groups": [
                reverse('group-detail', args=[g1.id]),
                reverse('group-detail', args=[g2.id]),
            ],
            "user_permissions": [
                reverse('permission-detail', args=[p1.id]),
                reverse('permission-detail', args=[p2.id]),
            ]
        }

    def test_create(self):
        url = reverse('user-list')

        # Json default format in settings.py
        response = self.client.post(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Can't check as a full equals because id, last_login... are autofields
        for k, v in self.data.items():
            # don't check group lists
            if k not in ("groups", "user_permissions"):
                self.assertEqual(response.data[k], self.data[k])

        self.assertEqual(len(response.data["groups"]),
                         len(self.data["groups"]))

        self.assertEqual(len(response.data["user_permissions"]),
                         len(self.data["user_permissions"]))

    def test_update(self):
        # Save first (We have already, but we will get the id)
        url = reverse('user-list')

        response = self.client.post(url, self.data)

        # Update later
        url = reverse('user-detail', args=[response.data["id"]])

        self.data["url"] = "http://batmanisnotbrucewayne.com"
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Can't check as a full equals because id, last_login... are autofields
        for k, v in self.data.items():
            # don't check group lists
            if k not in ("groups", "user_permissions"):
                self.assertEqual(response.data[k], self.data[k])

        self.assertEqual(len(response.data["groups"]),
                         len(self.data["groups"]))

        self.assertEqual(len(response.data["user_permissions"]),
                         len(self.data["user_permissions"]))

    def test_detail(self):
        # Save first (We have already, but we will get the id)
        url = reverse('user-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('user-detail', args=[response.data["id"]])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Can't check as a full equals because id, last_login... are autofields
        for k, v in self.data.items():
            # don't check group lists
            if k not in ("groups", "user_permissions"):
                self.assertEqual(response.data[k], self.data[k])

        self.assertEqual(len(response.data["groups"]),
                         len(self.data["groups"]))

        self.assertEqual(len(response.data["user_permissions"]),
                         len(self.data["user_permissions"]))

    def test_delete(self):
         # Save first (We have already, but we will get the id)
        url = reverse('user-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('user-detail', args=[response.data["id"]])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list(self):
        url = reverse('user-list')

        before = self.client.get(url).data["count"]

        # Sove N users
        number_users = random.randrange(20, 100)
        for i in range(number_users):
            self.data["username"] = "Batman-{0}".format(i)
            response = self.client.post(url, self.data)

        response = self.client.get(url)

        self.assertEqual(response.data["count"], number_users + before)


class ContentTypeAPITests(APITestCase):

    def setUp(self):
        # Set an user so we can use the API
        password = "I love my Xmen"
        u = User()
        u.username = "profesor-X"
        u.set_password(password)
        u.first_name = "Charles"
        u.last_name = "Xavier"
        u.is_superuser = True
        u.is_active = True
        u.is_staff = True
        u.save()

        # Login, we could use: 'force_authenticate' but we will login
        # as always, the 'classic' way, wiht DRF help
        self.client.login(username=u.username, password=password)

        self.data = {
            "name": "permission2",
            "app_label": "auth2",
            "model": "permission2"
        }

    def test_create(self):
        url = reverse('contenttype-list')

        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        for k, v in self.data.items():
            self.assertEqual(response.data[k], self.data[k])

    def test_update(self):
        # Save first (We have already, but we will get the id)
        url = reverse('contenttype-list')
        response = self.client.post(url, self.data)

        # Update later
        url = reverse('contenttype-detail', args=[response.data["id"]])

        self.data["name"] = "changed"
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        for k, v in self.data.items():
            self.assertEqual(response.data[k], self.data[k])

    def test_detail(self):
        url = reverse('contenttype-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('contenttype-detail', args=[response.data["id"]])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        for k, v in self.data.items():
            self.assertEqual(response.data[k], self.data[k])

    def test_delete(self):
        url = reverse('contenttype-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('contenttype-detail', args=[response.data["id"]])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list(self):
        url = reverse('contenttype-list')

        before = self.client.get(url).data["count"]

        number_content_type = random.randrange(20, 100)
        for i in range(number_content_type):
            self.data["name"] = "permission-{0}".format(i)
            self.data["app_label"] = "auth-{0}".format(i)

            response = self.client.post(url, self.data)

        response = self.client.get(url)

        self.assertEqual(response.data["count"], number_content_type + before)


class PermissionAPITests(APITestCase):

    def setUp(self):
        # Set an user so we can use the API
        password = "I love my Xmen"
        u = User()
        u.username = "profesor-X"
        u.set_password(password)
        u.first_name = "Charles"
        u.last_name = "Xavier"
        u.is_superuser = True
        u.is_active = True
        u.is_staff = True
        u.save()

        # Login, we could use: 'force_authenticate' but we will login
        # as always, the 'classic' way, wiht DRF help
        self.client.login(username=u.username, password=password)

        self.data = {
            "name": "Can add log entry test",
            "content_type": reverse('contenttype-detail', args=[1]),
            "codename": "add_logentry test",
        }

    def test_create(self):
        url = reverse('permission-list')

        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(response.data["codename"], self.data["codename"])
        self.assertEqual(urlparse(response.data["content_type"]).path,
                         self.data["content_type"])

    def test_update(self):
        # Save first (We have already, but we will get the id)
        url = reverse('permission-list')
        response = self.client.post(url, self.data)

        # Update later
        url = reverse('permission-detail', args=[response.data["id"]])

        self.data["content_type"] = reverse('contenttype-detail', args=[2])
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(response.data["codename"], self.data["codename"])
        self.assertEqual(urlparse(response.data["content_type"]).path,
                         self.data["content_type"])

    def test_detail(self):
        url = reverse('permission-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('permission-detail', args=[response.data["id"]])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(response.data["codename"], self.data["codename"])
        self.assertEqual(urlparse(response.data["content_type"]).path,
                         self.data["content_type"])

    def test_delete(self):
        url = reverse('permission-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('permission-detail', args=[response.data["id"]])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list(self):
        url = reverse('permission-list')

        before = self.client.get(url).data["count"]

        number_content_type = random.randrange(20, 100)
        for i in range(number_content_type):
            self.data["name"] = "name-{0}".format(i)
            self.data["codename"] = "codename-{0}".format(i)

            response = self.client.post(url, self.data)

        response = self.client.get(url)

        self.assertEqual(response.data["count"], number_content_type + before)


class GroupAPITests(APITestCase):

    def setUp(self):
        # Set an user so we can use the API
        password = "I love my Xmen"
        u = User()
        u.username = "profesor-X"
        u.set_password(password)
        u.first_name = "Charles"
        u.last_name = "Xavier"
        u.is_superuser = True
        u.is_active = True
        u.is_staff = True
        u.save()

        # Login, we could use: 'force_authenticate' but we will login
        # as always, the 'classic' way, wiht DRF help
        self.client.login(username=u.username, password=password)

        self.data = {
            "name": "Can add log entry test",
            "permissions": [
                reverse('permission-detail', args=[1]),
                reverse('permission-detail', args=[2]),
                reverse('permission-detail', args=[3]),
            ],
        }

    def test_create(self):
        url = reverse('group-list')

        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(len(response.data["permissions"]),
                         len(self.data["permissions"]))

    def test_update(self):
        # Save first (We have already, but we will get the id)
        url = reverse('group-list')
        response = self.client.post(url, self.data)

        # Update later
        url = reverse('group-detail', args=[response.data["id"]])

        new_permissions = [
            reverse('permission-detail', args=[3]),
            reverse('permission-detail', args=[4]),
        ]

        self.data["permissions"] = new_permissions
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(len(response.data["permissions"]),
                         len(new_permissions))

    def test_detail(self):
        url = reverse('group-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('group-detail', args=[response.data["id"]])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(len(response.data["permissions"]),
                         len(self.data["permissions"]))

    def test_delete(self):
        url = reverse('group-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('group-detail', args=[response.data["id"]])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list(self):
        url = reverse('group-list')

        before = self.client.get(url).data["count"]

        number_content_type = random.randrange(20, 100)
        for i in range(number_content_type):
            self.data["name"] = "name-{0}".format(i)

            response = self.client.post(url, self.data)

        response = self.client.get(url)

        self.assertEqual(response.data["count"], number_content_type + before)


class CompanyAPITests(APITestCase):

    def setUp(self):
        # Set an user so we can use the API
        password = "I love my Xmen"
        u = User()
        u.username = "profesor-X"
        u.set_password(password)
        u.first_name = "Charles"
        u.last_name = "Xavier"
        u.is_superuser = True
        u.is_active = True
        u.is_staff = True
        u.save()

        # Login, we could use: 'force_authenticate' but we will login
        # as always, the 'classic' way, wiht DRF help
        self.client.login(username=u.username, password=password)

        self.data = {
            "name": "Can add log entry test",
            "permissions": [
                reverse('permission-detail', args=[1]),
                reverse('permission-detail', args=[2]),
                reverse('permission-detail', args=[3]),
            ],
        }

    def test_create(self):
        url = reverse('company-list')

        response = self.client.post(url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(len(response.data["permissions"]),
                         len(self.data["permissions"]))

    def test_update(self):
        # Save first (We have already, but we will get the id)
        url = reverse('group-list')
        response = self.client.post(url, self.data)

        # Update later
        url = reverse('group-detail', args=[response.data["id"]])

        new_permissions = [
            reverse('permission-detail', args=[3]),
            reverse('permission-detail', args=[4]),
        ]

        self.data["permissions"] = new_permissions
        response = self.client.put(url, self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(len(response.data["permissions"]),
                         len(new_permissions))

    def test_detail(self):
        url = reverse('group-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('group-detail', args=[response.data["id"]])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(len(response.data["permissions"]),
                         len(self.data["permissions"]))

    def test_delete(self):
        url = reverse('group-list')
        response = self.client.post(url, self.data)

        # Get the details
        url = reverse('group-detail', args=[response.data["id"]])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_list(self):
        url = reverse('group-list')

        before = self.client.get(url).data["count"]

        number_content_type = random.randrange(20, 100)
        for i in range(number_content_type):
            self.data["name"] = "name-{0}".format(i)

            response = self.client.post(url, self.data)

        response = self.client.get(url)

        self.assertEqual(response.data["count"], number_content_type + before)