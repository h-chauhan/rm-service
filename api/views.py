from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .tasks import *

# Create your views here.
def getInternNotifications(request):
    saveInternNotifications()
    return JsonResponse({"success": True}, safe=False)

def getPlacementNotifications(request):
    savePlacementNotifications()
    return JsonResponse({"success": True}, safe=False)

def getInternJobs(request):
    saveInternJobs()
    return JsonResponse({"success": True}, safe=False)

def getPlacementJobs(request):
    savePlacementJobs()
    return JsonResponse({"success": True}, safe=False)