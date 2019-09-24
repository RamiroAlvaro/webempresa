from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    title = models.CharField('Título', max_length=200)
    content = RichTextField('Contenido')
    order = models.SmallIntegerField('Orden', default=0)
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de edición', auto_now=True)

    class Meta:
        verbose_name = 'página'
        verbose_name_plural = 'páginas'
        ordering = ['order', 'title']

    def __str__(self):
        return self.title
