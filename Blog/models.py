from django.db import models
from django.utils import timezone

# Django já tem modulo para usuário
class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Autor") # on_delete = remove em cascata todos que tem como chave secundária
    published_date = models.DateTimeField(blank=True, null=True,verbose_name="Data Publicação")
    created_date = models.DateTimeField(default=timezone.now, verbose_name="Data Criação")
    text = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()                             # salva no banco

    def __str__(self):
        #return self.title
        return '{} - {}'.format(self.title,self.author)