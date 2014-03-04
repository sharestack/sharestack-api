from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from members.models import User


@python_2_unicode_compatible # For Python 3.3 and 2.7
class Stack(models.Model):
    name = models.CharField(_("stack name"),
                            max_length=30,
                            null=False)
    description = models.TextField(_("stack description"),
                                   blank=True)
    private = models.BooleanField(_("private stack"),
                                  default=False)
    sharelink = models.URLField(_("sharing link"),
                                blank=True)
    owner =  models.ForeignKey(User, related_name='owned_stack')
    collaborators = models.ManyToManyField(
        User,
        related_name='collaboration_stack',
        blank=True)


    def __str__(self):
        return self.name


@python_2_unicode_compatible # For Python 3.3 and 2.7
class Instance(models.Model):
    name = models.CharField(_("instance name"),
                            max_length=30,
                            null=False)
    stack =  models.ForeignKey(Stack)

    def __str__(self):
        return self.name