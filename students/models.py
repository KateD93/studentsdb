#-*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Students(models.Model):
    """Students model"""

    class Meta(object):
        verbose_name = u"Студент"
        verbose_name_plural = u"Студенти"

    first_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Ім’я"
    )

    middle_name = models.CharField(
        max_length=256,
        blank=True,
        verbose_name=u"По-батькові",
        default=''
    )

    last_name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Прізвище"
    )

    ticket_number = models.CharField(
        max_length=256,
        blank=False,
        verbose_name=u"Білет"
    )

    st_photo = models.ImageField(
        name=None,
        verbose_name=u"Фото",
        height_field=30,
        width_field=40,
        null=False
    )

    date_of_birth = models.DateField(
        verbose_name=u"Дата народження",
        blank=False
    )

    notes = models.TextField(
        blank=True,
        verbose_name=u"Нотатки"
    )

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)
