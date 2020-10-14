from django.db import models
from users.models import User

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="titulo", max_length=100)
    date = models.DateField(verbose_name="data de postagem", auto_now_add=True)
    text = models.TextField(verbose_name="conteudo")

    def __str__(self):
        return "Titulo: " + self.title
