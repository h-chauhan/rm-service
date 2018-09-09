from .scrape import getNotifications, getJobs
from .models import PlacementNotification, PlacementJobOpening, InternNotification, InternJobOpening


def savePlacementNotifications():
    notifs = getNotifications("Placement")
    if len(notifs) > 0:
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


def saveInternNotifications():
    notifs = getNotifications("Internship")
    if len(notifs) > 0:
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


def savePlacementJobs():
    jobs = getJobs("Placement")
    if len(jobs) > 0:
        for job in jobs:
            jobOpening = PlacementJobOpening(
                name=job["name"],
                appDeadline=job["appDeadline"],
                dateOfVisit=job["dateOfVisit"],
                link=job["link"]
            )
            jobOpening.save()
        print("Placement Jobs saved!!!")


  

def saveInternJobs():
    jobs = getJobs("Internship")
    if len(jobs) > 0:
        for job in jobs:
            jobOpening = InternJobOpening(
                name=job["name"],
                appDeadline=job["appDeadline"],
                dateOfVisit=job["dateOfVisit"],
                link=job["link"]
            )
            jobOpening.save()
        print("Internship Jobs saved!!!")