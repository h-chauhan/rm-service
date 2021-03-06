from bs4 import BeautifulSoup
from robobrowser import RoboBrowser
from .account import *

import logging

def getNotifications(type):
    account = getAccount(type)
    logging.info({"Using Account": account})

    browser = login(type, account)
    params = getParams(type)
    browser.open(params["notifsUrl"])
    logging.info({"message": "Scraping RM Notifications", "url": params["notifsUrl"]})

    soup = browser.parsed

    ul = soup.find('ul',attrs={'class':'timeline'})
    li_time_label = ul.find_all('li',attrs={'class':'time-label'})
    div_timeline_item = ul.find_all('div',attrs={'class':'timeline-item'})

    notifs = []

    for i in range(len(li_time_label)):
        date = li_time_label[i].text.strip(' \t\n\r')
        time = div_timeline_item[i].span.text.strip(' \t\n\r').replace("&nbsp","").replace(";","")
        timelineHeader = div_timeline_item[i].find('h4',attrs={'class':'timeline-header'}).text.strip(' \t\n\r')
        timelineBody = div_timeline_item[i].find('div',attrs={'class':'timeline-body'}).text
        timelineHeaderUp = div_timeline_item[i].find('h3',attrs={'class':'timeline-header up'}).text.strip(' \t\n\r')
        timelineHeaderUp = timelineHeaderUp[len("Posted by : \n              \n              "):]
        notifs.append({
            "date": date,
            "time": time,
            "heading": timelineHeader,
            "body": timelineBody,
            "poster": timelineHeaderUp
        })

    logging.info({"message": "Notifications Scraped!!!"})
    return notifs

def getJobs(type):
    account = getAccount(type)
    logging.info({"Using Account": account})

    browser = login(type, account)
    params = getParams(type)
    browser.open(params["jobsUrl"])
    logging.info({"message": "Scraping RM Jobs", "url": params["jobsUrl"]})

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

    logging.info({"message": "Jobs Scraped!!!"})
    return companyDetails
