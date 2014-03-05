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
    # Specs
    ram = models.CharField(_("ram specs"), max_length=60, blank=True)
    cpu = models.CharField(_("cpu specs"), max_length=60, blank=True)
    hdd = models.CharField(_("hdd specs"), max_length=60, blank=True)
    instance_type = models.CharField(_("instance type"),
                                     max_length=60,
                                     blank=True)
    provider = models.CharField(_("provider name"), max_length=60, blank=True)
    provider_name = models.CharField(_("provider instance name"),
                                     max_length=60,
                                     blank=True)
    description = models.TextField(_("instance description"), blank=True)

    stack =  models.ForeignKey(Stack)


    def __str__(self):
        return self.name