from django.db import models



class post(models.Model):
    nome = models.CharField (max_length=20,blank=False, null=True ,verbose_name='Nome do autor')
    titulo = models.CharField(max_length=30, blank=False, null=True ,verbose_name='Titulo da postagem')
    descricao = models.TextField(max_length=300, blank=False, null=True, verbose_name='Descrição' )
    link = models.TextField(blank=False,null=True, verbose_name='Link para direcionar o usuario')
    link_tumb = models.TextField(blank=False,null=True, verbose_name='Link pro Wallpaper dessa postagem')
    date = models.DateField(auto_now=True)

 

    def __str__(self): 
        return self.titulo



 
# Create your models here.
