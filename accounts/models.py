from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name  = models.CharField(max_length = 30)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length = 30)
    publication_date = models.DateTimeField()
    total_votes  = models.IntegerField(default=0)
    image = models.ImageField(upload_to = 'images/')
    icon = models.ImageField(upload_to = 'iamges/')
    body = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    hunter = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def summary(self):
        return self.body[:100]
    def pub(self ):
        return self.publication_date.strftime('%b %e %Y')
    
    def __str__(self):
        return self.title

