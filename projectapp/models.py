from django.db import models

# Create your models here.


class NewsModel(models.Model):
    news_heading = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    date = models.DateField()
    image = models.ImageField(upload_to='images/')
    
    def __str__(self):
        return self.news_heading

class AppointmentModel(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=10)  
    place = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    date = models.DateField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

    
