from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible  # For Python 3.3 and 2.7
class TechType(models.Model):
    name = models.CharField(_("tech type name"),
                            max_length=30,
                            null=False)
    description = models.TextField(_("tech type description"), blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible  # For Python 3.3 and 2.7
class Tech(models.Model):
    name = models.CharField(_("tech name"),
                            max_length=30,
                            null=False)
    url = models.URLField(_("tech site"), blank=True)
    description = models.TextField(_("tech description"), blank=True)
    logo = models.URLField(_("url to the image"), blank=True)
    open_source = models.BooleanField(_("open source tech"), default=False)
    repo = models.URLField(_("tech repo"), blank=True)
    types = models.ManyToManyField(TechType, blank=True)
    tech_components = models.ManyToManyField("self",
                                             symmetrical=False,
                                             blank=True)

    def __str__(self):
        return self.name


@python_2_unicode_compatible  # For Python 3.3 and 2.7
class Component(models.Model):
    name = models.CharField(_("component name"),
                            max_length=30,
                            null=False)
    version = models.CharField(_("tech version"),
                               max_length=15)
    config = models.TextField(_("configuration"), blank=True)
    description = models.TextField(_("description"), blank=True)
    tech = models.ForeignKey(Tech)

    def __str__(self):
        return self.name
