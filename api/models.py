from django.db import models

# Create your models here.
class RMAccount(models.Model):
    type = models.CharField(max_length=10, choices=(('Internship', 'Internship'), ('Placement', 'Placement')))
    username = models.CharField(max_length=12)
    password = models.TextField()

    def __str__(self):
        return self.type + " : " + self.username

class Notification(models.Model):
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    header = models.CharField(max_length=200)
    body  = models.TextField()
    poster = models.CharField(max_length=200)

    def __str__(self):
        return self.date + " : " + self.time

class PlacementNotification(Notification):
    pass
    
class InternNotification(Notification):
    pass

class JobOpening(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.CharField(max_length=100)
    dateOfVisit = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name

class PlacementJobOpening(JobOpening):
    pass
    
class InternJobOpening(JobOpening):
    pass
