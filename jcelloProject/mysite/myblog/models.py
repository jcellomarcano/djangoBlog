from django.db import models #para erencia de nuestra base de datos
from django.contrib.auth.models import User #modelo para el manejor de usuarios en Django
from django.template.defaultfilters import slugify
from django.dispatch import receiver
from django.db.models.signals import post_delete

# Create your models here.

class UserProfile(models.Model):

    nombre = models.CharField(max_length = 300)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nombre)


class Post(models.Model):

    titulo = models.CharField(max_length = 200)
    slug = models.SlugField(max_length = 100, unique = True)
    cuerpo = models.TextField()
    publicado = models.DateTimeField(auto_now_add = True)
    presentar = models.BooleanField(blank = True, null = False, default = True)
    autor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    """@receiver(post_delete, sender=Profile)
    def post_delete_user(sender, instance, *args, **kwargs):
        if instance.user:
            instance.user.delete()"""

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.titulo)

        super(Post, self).save(*args, **kwargs)
