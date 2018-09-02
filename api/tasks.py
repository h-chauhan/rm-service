from celery import shared_task
from .scrape import getNotifications, getJobs
from .models import PlacementNotification, PlacementJobOpening, InternNotification, InternJobOpening

@shared_task
def savePlacementNotifications():
    notifs = getNotifications("Placement")
    if len(notifs) > 0:
        PlacementNotification.objects.all().delete()
        for notif in notifs:
            notification = PlacementNotification(
                date=notif["date"],
                time=notif["time"],
                heading=notif["heading"],
                body=notif["body"],
                poster=notif["poster"]
            )
            notification.save()
        print("Placement Notifications saved!!!")

@shared_task
def saveInternNotifications():
    notifs = getNotifications("Internship")
    if len(notifs) > 0:
        InternNotification.objects.all().delete()
        for notif in notifs:
            notification = InternNotification(
                date=notif["date"],
                time=notif["time"],
                heading=notif["heading"],
                body=notif["body"],
                poster=notif["poster"]
            )
            notification.save()
        print("Internship Notifications saved!!!")

@shared_task
def savePlacementJobs():
    jobs = getJobs("Placement")
    if len(jobs) > 0:
        PlacementJobOpening.objects.all().delete()
        for job in jobs:
            jobOpening = PlacementJobOpening(
                name=job["name"],
                appDeadline=job["appDeadline"],
                dateOfVisit=job["dateOfVisit"],
                link=job["link"]
            )
            jobOpening.save()
        print("Placement Jobs saved!!!")

@shared_task
def saveInternJobs():
    jobs = getJobs("Internship")
    if len(jobs) > 0:
        InternJobOpening.objects.all().delete()
        for job in jobs:
            jobOpening = InternJobOpening(
                name=job["name"],
                appDeadline=job["appDeadline"],
                dateOfVisit=job["dateOfVisit"],
                link=job["link"]
            )
            jobOpening.save()
        print("Internship Jobs saved!!!")