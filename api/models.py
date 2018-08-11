from django.db import models

# Create your models here.
class RMCredentialsSet(models.Model):
    type = models.CharField(max_length=10, choices=(('Internship', 'Internship'), ('Placement', 'Placement')))
    username = models.CharField(max_length=12)
    password = models.TextField()

    def __str__(self):
        return self.type + " : " + self.username