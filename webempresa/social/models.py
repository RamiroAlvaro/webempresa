from django.db import models


class Link(models.Model):
    key = models.SlugField('Nombre clave', max_length=100, unique=True)
    name = models.CharField('Red social', max_length=200)
    url = models.URLField('Enlace', max_length=200, null=True, blank=True)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de edición', auto_now=True)

    class Meta:
        verbose_name = 'enlace'
        verbose_name_plural = 'enlaces'
        ordering = ['name']

    def __str__(self):
        return self.name
