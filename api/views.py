from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .scrape import *

# Create your views here.
def getInternNotifications(request):
    result = getNotifications("Internship")
    return JsonResponse(result, safe=False)

def getNotifications(request):
    result = getNotifications("Placement")
    return JsonResponse(result, safe=False)

def getInternJobs(request):
    result = getJobs("Internship")
    return JsonResponse(result, safe=False)

def getJobs(request):
    result = getJobs("Placement")
    return JsonResponse(result, safe=False)
