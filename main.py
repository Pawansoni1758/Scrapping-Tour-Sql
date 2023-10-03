import time
import requests
import selectorlib
import os
import smtplib, ssl
import sqlite3

URL = "https://programmer100.pythonanywhere.com/tours/"
db = sqlite3.connect("data.db")

def scrape(url):
    """scrape the page source from the url """
    response = requests.get(url)
    source = response.text
    return source


def extract(source):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(source)['tours']
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    user_name = "pawan2004soni@gmail.com"
    password = os.getenv("PASSWORD")
    receiver = "pawan2004soni@gmail.com"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)
    print("email was sent")


def store(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    cursor = db.cursor()
    cursor.execute("insert into events values(?,?,?)", row)
    db.commit()


def read(extracted):
    row = extracted.split(",")
    row = [item.strip() for item in row]
    band, city, date = row
    cursor = db.cursor()
    cursor.execute("select * from events where band=? and city=? and date=?",
                   (band, city, date))
    rows = cursor.fetchall()
    return rows


body = "subject: New event" + '\n' + "Event name"

if __name__ == "__main__":
    while True:
        scraped = scrape(URL)
        extracted = extract(scraped)
        print(extracted)
        if extracted != "No upcoming tours":
            row = read(extracted)
            if not row:
                store(extracted)
                send_email(message=body)
        time.sleep(2)
