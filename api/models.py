from django.db import models
from rmbot.firebase import db
from google.cloud.exceptions import NotFound

# Create your models here.
class RMAccount(models.Model):
    type = models.CharField(max_length=10, choices=(('Internship', 'Internship'), ('Placement', 'Placement')))
    username = models.CharField(max_length=12)
    password = models.TextField()

    def __str__(self):
        return self.type + " : " + self.username

    @staticmethod
    def from_dict(type, dict):
        account = RMAccount(type)
        account.username, account.password = dict['username'], dict['password']
        return account 

    @staticmethod
    def get(type):
        ref = db.collection(u'rm_accounts').document(type)
        try:
            doc = ref.get()
            return RMAccount.from_dict(type, doc.to_dict())
        except NotFound:
            return RMAccount(type)

    def save(self):
        ref = db.collection(u'rm_accounts').document(self.type)
        ref.set({
            u'username': self.username,
            u'password': self.password
        })

class Notification(models.Model):
    date = models.CharField(max_length=50)
    time = models.CharField(max_length=50)
    heading = models.CharField(max_length=200)
    body  = models.TextField()
    poster = models.CharField(max_length=200)

    def __str__(self):
        return self.date + " : " + self.time

    def to_dict(self):
        return {
            "date": self.date,
            "time": self.time,
            "heading": self.heading,
            "body": self.body,
            "poster": self.poster
        }

class PlacementNotification(Notification):
    def save(self):
        ref = db.collection(u'placement_notifications').document(self.__str__())
        ref.set(self.to_dict())

class InternNotification(Notification):
    def save(self):
        ref = db.collection(u'internship_notifications').document(self.__str__())
        ref.set(self.to_dict())

class JobOpening(models.Model):
    name = models.CharField(max_length=100)
    appDeadline = models.CharField(max_length=100)
    dateOfVisit = models.CharField(max_length=100)
    link = models.URLField()

    def __str__(self):
        return self.name

    def to_dict(self):
        return {
            "name": self.name,
            "appDeadline": self.appDeadline,
            "dateOfVisit": self.dateOfVisit,
            "link": self.link
        }

class PlacementJobOpening(JobOpening):
    def save(self):
        ref = db.collection(u'placement_jobs').document(self.__str__())
        ref.set(self.to_dict())

class InternJobOpening(JobOpening):
    def save(self):
        ref = db.collection(u'internship_jobs').document(self.__str__())
        ref.set(self.to_dict())
