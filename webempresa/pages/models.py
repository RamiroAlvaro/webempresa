from django.db import models


class Page(models.Model):
    title = models.CharField('Título', max_length=200)
    content = models.TextField('Contenido')
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de edición', auto_now=True)

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['title']

    def __str__(self):
        return self.title
