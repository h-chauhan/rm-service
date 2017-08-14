from django.shortcuts import render
from django.http import HttpResponse

from robobrowser import RoboBrowser

# Create your views here.
def getNotifications(request):
    loginUrl = "http://tnp.dtu.ac.in/rm_2016-17/login/"
    loginUsername = "2K14/SE/027"
    loginPassword = "RANA27RM"

    notifsUrl = "http://tnp.dtu.ac.in/rm_2016-17/student/"

    browser = RoboBrowser(history=True)
    browser.open(loginUrl)

    form = browser.get_form(0)
    form['student_username_rollnumber'].value = loginUsername
    form['student_password'].value = loginPassword
    browser.submit_form(form)

    browser.open(notifsUrl)

    return HttpResponse(browser.parsed)

def getInternNotifications(request):
    internLoginUrl = "http://tnp.dtu.ac.in/rm_2016-17/intern/intern_login"
    internLoginUsername = "2K15/EC/159"
    internLoginPassword = "password"

    internNotifsUrl = "http://tnp.dtu.ac.in/rm_2016-17/intern/intern_student"

    browser = RoboBrowser(history=True)
    browser.open(internLoginUrl)

    form = browser.get_form(0)
    form['intern_student_username_rollnumber'].value = internLoginUsername
    form['intern_student_password'].value = internLoginPassword
    browser.submit_form(form)

    browser.open(internNotifsUrl)

    return HttpResponse(browser.parsed)

def getJobs(request):
    loginUrl = "http://tnp.dtu.ac.in/rm_2016-17/login/"
    loginUsername = "2K14/SE/027"
    loginPassword = "RANA27RM"

    jobsUrl = "http://tnp.dtu.ac.in/rm_2016-17/student/job_openings/"

    browser = RoboBrowser(history=True)
    browser.open(loginUrl)

    form = browser.get_form(0)
    form['student_username_rollnumber'].value = loginUsername
    form['student_password'].value = loginPassword
    browser.submit_form(form)

    browser.open(jobsUrl)

    return HttpResponse(browser.parsed)

def getInternJobs(request):
    internLoginUrl = "http://tnp.dtu.ac.in/rm_2016-17/intern/intern_login"
    internLoginUsername = "2K15/EC/159"
    internLoginPassword = "password"

    internJobsUrl = "http://tnp.dtu.ac.in/rm_2016-17/intern/intern_student/job_openings"

    browser = RoboBrowser(history=True)
    browser.open(internLoginUrl)

    form = browser.get_form(0)
    form['intern_student_username_rollnumber'].value = internLoginUsername
    form['intern_student_password'].value = internLoginPassword
    browser.submit_form(form)

    browser.open(internJobsUrl)

    return HttpResponse(browser.parsed)
