from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup

from robobrowser import RoboBrowser

# Create your views here.
def getNotifications(request):
    loginUrl = "http://tnp.dtu.ac.in/rm_2016-17/login/"
    loginUsername = "2K15/EC/159"
    loginPassword = "password"

    notifsUrl = "http://tnp.dtu.ac.in/rm_2016-17/student/"

    browser = RoboBrowser(history=True)
    browser.open(loginUrl)

    form = browser.get_form(0)
    form['student_username_rollnumber'].value = loginUsername
    form['student_password'].value = loginPassword
    browser.submit_form(form)

    browser.open(notifsUrl)
    soup = browser.parsed

    ul = soup.find('ul',attrs={'class':'timeline'})

    li_time_label = ul.find_all('li',attrs={'class':'time-label'})
    div_timeline_item = ul.find_all('div',attrs={'class':'timeline-item'})

    result = []

    for i in range(len(li_time_label)):
        date = li_time_label[i].text.strip(' \t\n\r')
        time = div_timeline_item[i].span.text.strip(' \t\n\r').replace("&nbsp","").replace(";","")
        timelineHeader = div_timeline_item[i].find('h4',attrs={'class':'timeline-header'}).text.strip(' \t\n\r')
        timelineBody = div_timeline_item[i].find('div',attrs={'class':'timeline-body'}).text
        timelineHeaderUp = div_timeline_item[i].find('h3',attrs={'class':'timeline-header up'}).text.strip(' \t\n\r')
        timelineHeaderUp = timelineHeaderUp[len("Posted by : \n              \n              "):]
        result.append({
            "date": date,
            "time": time,
            "heading": timelineHeader,
            "body": timelineBody,
            "poster": timelineHeaderUp
        })

    return JsonResponse(result, safe=False)

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
    soup = browser.parsed

    ul = soup.find('ul',attrs={'class':'timeline'})

    li_time_label = ul.find_all('li',attrs={'class':'time-label'})
    div_timeline_item = ul.find_all('div',attrs={'class':'timeline-item'})

    result = []

    for i in range(len(li_time_label)):
        date = li_time_label[i].text.strip(' \t\n\r')
        time = div_timeline_item[i].span.text.strip(' \t\n\r').replace("&nbsp","").replace(";","")
        timelineHeader = div_timeline_item[i].find('h4',attrs={'class':'timeline-header'}).text.strip(' \t\n\r')
        timelineBody = div_timeline_item[i].find('div',attrs={'class':'timeline-body'}).text
        timelineHeaderUp = div_timeline_item[i].find('h3',attrs={'class':'timeline-header up'}).text.strip(' \t\n\r')
        timelineHeaderUp = timelineHeaderUp[len("Posted by : \n              \n              "):]
        result.append({
            "date": date,
            "time": time,
            "heading": timelineHeader,
            "body": timelineBody,
            "poster": timelineHeaderUp
        })

    return JsonResponse(result, safe=False)

def getJobs(request):
    loginUrl = "http://tnp.dtu.ac.in/rm_2016-17/login/"
    loginUsername = "2K15/EC/159"
    loginPassword = "password"

    jobsUrl = "http://tnp.dtu.ac.in/rm_2016-17/student/job_openings/"

    browser = RoboBrowser(history=True)
    browser.open(loginUrl)

    form = browser.get_form(0)
    form['student_username_rollnumber'].value = loginUsername
    form['student_password'].value = loginPassword
    browser.submit_form(form)

    browser.open(jobsUrl)
    soup = browser.parsed

    table_jobopenings = soup.find('table',attrs={'id':'jobs_search'})
    trs = table_jobopenings.find_all('tr')

    companyDetails = []

    for i in range(1, len(trs)):
        tds = trs[i].find_all('td')
        if tds[3].find('i')['class'][1] == 'fa-check':
            companyDetails.append({
                "name": tds[0].text,
                "appDeadline": tds[2].text,
                "dateOfVisit": tds[6].text,
                "link": trs[i]['onclick'].replace("void window.open('","").replace("')",""),
            })

    return JsonResponse(companyDetails, safe=False)

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
    soup = browser.parsed

    table_jobopenings = soup.find('table',attrs={'id':'jobs_search'})
    trs = table_jobopenings.find_all('tr')

    companyDetails = []

    for i in range(1, len(trs)):
        tds = trs[i].find_all('td')
        if tds[3].find('i')['class'][1] == 'fa-check':
            companyDetails.append({
                "name": tds[0].text,
                "appDeadline": tds[2].text,
                "dateOfVisit": tds[6].text,
                "link": trs[i]['onclick'].replace("void window.open('","").replace("')",""),
            })

    return JsonResponse(companyDetails, safe=False)
