from django.db import models

# Create your models here.
class Venue(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=1000)
    zip_code = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, blank=True)
    web = models.URLField('Website Address', blank=True)
    email_address = models.EmailField('Email Address', blank=True)
   
    def __str__(self):
        return self.name 

class MyClubUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField('Email Address')

    def __str__(self):
        return self.first_name +' '+ self.last_name 

class Event(models.Model):
    name = models.CharField('Event Name', max_length=120)
    event_date = models.DateTimeField('Event_Date')
    venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
    #venue = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank=True)

    def __str__(self):
        return self.name
