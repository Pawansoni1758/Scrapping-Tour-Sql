import requests
import selectorlib
import time
import sqlite3

URL = "https://programmer100.pythonanywhere.com/"
db = sqlite3.connect("data.db", timeout=30)

def scrap(url):
    response = requests.get(url)
    return response.text


def extract(source):
    extrator = selectorlib.Extractor.from_yaml_file("temp.yaml")
    value = extrator.extract(source)['tours']
    return value

def store(extracted):
    now = time.strftime('%y-%m-%d-%H:%M:%S')
    row = extracted
    cursor = db.cursor()
    cursor.execute('insert into temp values(?, ?)', (now, row))
    db.commit()
    cursor.close()


if __name__ == "__main__":
    while True:
        scraped = scrap(URL)
        extracted = extract(scraped)
        print(extracted)
        store(extracted)
