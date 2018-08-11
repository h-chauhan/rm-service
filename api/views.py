from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .scrape import *

# Create your views here.
def getInternNotifications(request):
    iaccount = Account.getAccount("Internship")
    ibrowser = login("Internship", iaccount)
    result = parseNotifications("Internship", ibrowser)
    return JsonResponse(result, safe=False)

def getNotifications(request):
    paccount = Account.getAccount("Placement")
    pbrowser = login("Placement", paccount)
    result = parseNotifications("Placement", pbrowser)
    return JsonResponse(result, safe=False)

def getInternJobs(request):
    iaccount = Account.getAccount("Internship")
    ibrowser = login("Internship", iaccount)
    result = parseJobs("Internship", ibrowser)
    return JsonResponse(result, safe=False)

def getJobs(request):
    paccount = Account.getAccount("Placement")
    pbrowser = login("Placement", paccount)
    result = parseJobs("Placement", pbrowser)
    return JsonResponse(result, safe=False)
