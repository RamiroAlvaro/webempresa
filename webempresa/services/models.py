from django.db import models


class Service(models.Model):
    title = models.CharField('Título', max_length=200)
    subtitle = models.CharField('Subtítulo', max_length=200)
    content = models.TextField('Contenido')
    image = models.ImageField('Imagen', upload_to='services')
    created = models.DateTimeField('Fecha de creación', auto_now_add=True)
    updated = models.DateTimeField('Fecha de edición', auto_now=True)

    class Meta:
        verbose_name = 'servicio'
        verbose_name_plural = 'servicios'
        ordering = ['-created']

    def __str__(self):
        return self.title
