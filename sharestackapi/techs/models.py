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
