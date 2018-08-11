from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .scrape import *

iaccount = Account.getAccount("Internship")
ibrowser = login("Internship", iaccount)
paccount = Account.getAccount("Placement")
pbrowser = login("Placement", paccount)

# Create your views here.
def getInternNotifications(request):
    result = parseNotifications("Internship", ibrowser)
    return JsonResponse(result, safe=False)

def getNotifications(request):
    result = parseNotifications("Placement", pbrowser)
    return JsonResponse(result, safe=False)

def getInternJobs(request):
    result = parseJobs("Internship", ibrowser)
    return JsonResponse(result, safe=False)

def getJobs(request):
    result = parseJobs("Placement", pbrowser)
    return JsonResponse(result, safe=False)
