from django.db import models

# Create your models here.
class course(models.Model):
    code = models.CharField(max_length=150)
    name = models.TextField(max_length=150)
    hour = models.IntegerField(max_length=3)
    credits = models.IntegerField(max_length=2)
    state = models.CharField(max_length=150)

# Create your models here.
class career(models.Model):
    name = models.TextField(max_length=150)
    shortname = models.TextField(max_length=100)
    image = models.ImageField(default='null', verbose_name="Miniatura", upload_to="career")
    state = models.CharField(max_length=150)
