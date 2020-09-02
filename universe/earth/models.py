from django.db import models
from django.utils.translation import gettext_lazy as _


class Human(models.Model):
    class BloodType(models.TextChoices):
        TYPE_A = 'A', _('A型')
        TYPE_B = 'B', _('B型')
        TYPE_O = 'O', _('O型')
        TYPE_AB = 'AB', _('AB型')

    name = models.CharField(_("名前"), max_length=50)
    birthday = models.DateField(_("誕生日"))
    height = models.DecimalField(_("身長"), max_digits=5, decimal_places=2)
    weight = models.IntegerField(_("体重"))
    blood_type = models.CharField(_("血液型"), choices=BloodType.choices, max_length=50)
