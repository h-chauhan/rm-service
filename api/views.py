from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers

from .scrape import *
from .models import *
from .serializers import *
from .tasks import *

# Create your views here.
def getInternNotifications(request):
    notifs = InternNotification.objects.all()
    serializer = InternNotificationSerializer(notifs, many=True)
    return JsonResponse(serializer.data, safe=False)

def getPlacementNotifications(request):
    notifs = PlacementNotification.objects.all()
    serializer = PlacementNotificationSerializer(notifs, many=True)
    return JsonResponse(serializer.data, safe=False)

def getInternJobs(request):
    jobs = InternJobOpening.objects.all()
    serializers = InternJobSerializer(jobs, many=True)
    return JsonResponse(serializers.data, safe=False)

def getPlacementJobs(request):
    jobs = PlacementJobOpening.objects.all()
    serializers = PlacementJobSerializer(jobs, many=True)
    return JsonResponse(serializers.data, safe=False)

savePlacementNotifications()
savePlacementJobs()
saveInternNotifications()
saveInternJobs()