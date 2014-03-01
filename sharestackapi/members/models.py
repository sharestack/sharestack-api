import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible # For Python 3.3 abd 2.7
class User(AbstractUser):
    url = models.URLField(_("url"),
                        blank=True)
    gravatar = models.EmailField(_("gravatar"),
                                blank=True)
    activation_token = models.CharField(
        _("activation_token"),
        max_length=40,
        default=uuid.uuid4(),
        blank=True
    )
    reset_password_token = models.CharField(
        _("reset_password_token"),
        max_length=40,
        default=uuid.uuid4(),
        blank=True
    )


    def __str__(self):
        return self.username