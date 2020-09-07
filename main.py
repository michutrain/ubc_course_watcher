import requests
import bs4
import smtplib
from time import sleep

user_email = "<YOUR EMAIL HERE>"
course_url = "https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=CPSC&course=344&section=101"

subject = "Empty Seat in Course!!"
body = "There is a spot in the course: "
server_email = "course.sniper.ubc@gmail.com"
server_password = "chiggenbutt1"
email_sent = False
timer = 60

def main():
    res = requests.get(course_url)
    soup = bs4.BeautifulSoup(res.text, 'html')
    table = soup.select('tr')
    seats = int(table[5].getText().split(":", 1)[1])
    title = soup.select('h4')
    course_title = title[0].getText()
    while (not email_sent):
        if seats > 0:
            send_email(course_title)
            break
        sleep(timer)

def send_email(course_title):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(server_email, server_password)
        message = 'Subject: {}\n\n{}'.format(subject, body + course_title)
        server.sendmail(server_email, user_email, message)
        server.quit()
        print("Email Sent")
        global email_sent
        email_sent = True
    except:
        print("Failed to send Email")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
