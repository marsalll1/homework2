from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    stock = models.IntegerField(default=0)
    cover_image = models.FileField(upload_to='covers/', null=True, blank=True)
    publisher_email = models.EmailField(null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    genre = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.title
