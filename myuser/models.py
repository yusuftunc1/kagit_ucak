from tabnanny import verbose
from django.db import models

# Create your models here.


class myuser(models.Model):
    username = models.CharField(blank=False, null=False, max_length=150, verbose_name='Kullanıcı adı')
    firstname = models.CharField(blank= False, null= False, max_length=150, verbose_name= 'İsim')
    lastname = models.CharField(blank= False, null= False, max_length=150, verbose_name= 'Soy isim')
    email = models.EmailField(blank= False, null= False, verbose_name= 'Email')
    phonenum = models.CharField(blank= False, null= False, max_length=50, verbose_name= 'telefon numarası')
    range = models.IntegerField(blank= True, null= True, verbose_name= 'Mesafe')
    flighttime = models.DecimalField(blank= True, null= True,decimal_places= 2, max_digits=10, verbose_name= 'uçuş süresi')
    score = models.IntegerField(blank= True, null= True, verbose_name= 'Puanı')

