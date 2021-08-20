from django.db import models

# Create your models here.

class Project(models.Model):
# Agregamos verbose_name a cada campo para setear el nombre de la propiedad.
    title = models.CharField(verbose_name='Título', max_length=50)
    description = models.TextField(verbose_name='Descripción')
    image = models.ImageField(verbose_name='Imagen', upload_to='project')
    link = models.URLField(null=True, blank=True, verbose_name="Dirección web")
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')

# creamos la clase Meta para establecer metadatos
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        # Le establecemos el orden en que van a aparecer en el admin
        ordering = ['-created']
        # verbose_name = 'Nuez'
        # verbose_name_plural = 'Nueces'

# Definimos el método __str__ para ver el titulo de la instancia y no el hash
    def __str__(self) -> str:
        return self.title
