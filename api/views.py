import time
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from sentry_sdk import capture_message

from .scrape import getNotifications, getJobs

# Create your views here.
def getInternNotifications(request):
    requestStartTime = time.time()
    result = getNotifications("Internship")
    capture_message({ 
        "message": "request",
        "request": request,
        "duration": time.time() - requestStartTime
    }, level="info")
    return JsonResponse(result, safe=False)

def getPlacementNotifications(request):
    requestStartTime = time.time()
    result = getNotifications("Placement")
    capture_message({          
        "message": "request",         
        "request": request,         
        "duration": time.time() - requestStartTime     
    }, level="info")
    return JsonResponse(result, safe=False)

def getInternJobs(request):
    requestStartTime = time.time()
    result = getJobs("Internship")
    capture_message({          
        "message": "request",         
        "request": request,         
        "duration": time.time() - requestStartTime     
    }, level="info")
    return JsonResponse(result, safe=False)

def getPlacementJobs(request):
    requestStartTime = time.time()
    result = getJobs("Placement")
    capture_message({          
        "message": "request",         
        "request": request,         
        "duration": time.time() - requestStartTime     
    }, level="info")
    return JsonResponse(result, safe=False)