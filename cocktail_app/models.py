from django.db import models

# Create your models here.
class Cocktail(models.Model):
    name=models.CharField(max_length=30,blank=True,null=True)
    category=models.CharField(max_length=30,blank=True,null=True)
    ingredients=models.CharField(max_length=30,blank=True,null=True)
    instructions=models.CharField(max_length=30,blank=True,null=True)
    measures=models.CharField(max_length=30,blank=True,null=True)
    slug=models.SlugField(default='test')
    image_url=models.CharField(max_length=50,blank=True,null=True)

    def __str__(self):
        return self.name

