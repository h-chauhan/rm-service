from .models import RMAccount
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser

def getParams(type):
    return {
        "loginUrl": "http://tnp.dtu.ac.in/rm_2016-17/intern/intern_login",
        "username_field": "intern_student_username_rollnumber",
        "password_field": "intern_student_password",
        "notifsUrl": "http://tnp.dtu.ac.in/rm_2016-17/intern/intern_student",
        "jobsUrl": "http://tnp.dtu.ac.in/rm_2016-17/intern/intern_student/job_openings",
        "year": "2K16"
    } if type == "Internship" else {
        "loginUrl": "http://tnp.dtu.ac.in/rm_2016-17/login",
        "username_field": "student_username_rollnumber",
        "password_field": "student_password",
        "notifsUrl": "http://tnp.dtu.ac.in/rm_2016-17/student",
        "jobsUrl": "http://tnp.dtu.ac.in/rm_2016-17/student/job_openings/",
        "year": "2K15"
    }

def login(type, account):
    params = getParams(type)
    browser = RoboBrowser(history=True, parser="html.parser")
    browser.open(params["loginUrl"])
    form = browser.get_form(0)
    form[params["username_field"]].value = account.username
    form[params["password_field"]].value = account.password
    browser.submit_form(form)
    return browser

def checkLogin(type, username, password):
    params = getParams(type)
    account = RMAccount(type=type, username=username, password=password)
    browser = login(type, account)
    browser.open(params["notifsUrl"])
    soup = browser.parsed
    ul = soup.find('ul',attrs={'class':'timeline'})
    return True if ul else False

def findNewAccount(type):
    params = getParams(type)
    branches = ["CO", "SE", "IT", "EC", "EL", "EE", "CE", "PS", "BT", "EP", "MC", "ME", "AM", "PE", "EN"]
    for branch in branches:
        for i in range(1, 100):
            rollno = "00" + str(i) if i < 10 else "0" + str(i)
            username = params["year"] + "/" + branch + "/" + rollno
            password = "password"
            if checkLogin(type, username, password):
                account, created = RMAccount.objects.get_or_create(type=type)
                account.username = username
                account.password = password
                account.save()
                return account
    return None

def getAccount(type):
    if RMAccount.objects.filter(type=type).exists():
        account = RMAccount.objects.get(type=type)
        if checkLogin(type, account.username, account.password):
            return account
    return findNewAccount(type)
