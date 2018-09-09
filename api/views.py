from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .scrape import getNotifications, getJobs

# Create your views here.
def getInternNotifications(request):
    result = getNotifications("Internship")
    return JsonResponse(result, safe=False)

def getPlacementNotifications(request):
    result = getNotifications("Placement")
    return JsonResponse(result, safe=False)

def getInternJobs(request):
    result = getJobs("Internship")
    return JsonResponse(result, safe=False)

def getPlacementJobs(request):
    result = getJobs("Placement")
    return JsonResponse(result, safe=False)