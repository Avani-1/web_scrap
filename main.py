'''
Event Name
Event Date(s)
Location (if applicable)
Website URL
Description
!!! Key Speakers
Agenda/Schedule
Registration Details
Pricing 
Categories
Audience type 
'''

from bs4 import BeautifulSoup as bs
import requests
import selenium as sel
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from datetime import datetime
from datetime import datetime
import pytz
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

html_text = requests.get('https://www.townscript.com/in/delhi/paid--business').text
soup = bs(html_text, 'lxml')

events = soup.find_all('div', class_ = 'lg:w-1/3 md:w-2/5 w-full px-3 my-3 fadeIn ng-star-inserted',limit=5)
dict = {}
i=1
for event in events:
    dict_temp = {}
    event_name = event.div.a.div.find('div', class_='card-body overflow-hidden w-full flex flex-wrap flex-col px-4 pb-4 md:px-5 md:pb-5 ng-star-inserted').div.div.div.span.string
    event_date = event.div.a.div.find('div', class_='card-body overflow-hidden w-full flex flex-wrap flex-col px-4 pb-4 md:px-5 md:pb-5 ng-star-inserted').div.find('div',class_='secondary-details fadeIn animation-delay flex items-center justify-start text-xs md:text-sm text-gray-800 mt-2 md:mt-3').div.span.string
    location = event.div.a.div.find('div', class_='card-body overflow-hidden w-full flex flex-wrap flex-col px-4 pb-4 md:px-5 md:pb-5 ng-star-inserted').div.find('div',class_='secondary-details fadeIn animation-delay flex items-center justify-start text-xs md:text-sm text-gray-800 mt-2 md:mt-3').find('div', class_='location overflow-hidden whitespace-no-wrap ng-star-inserted').span.string
    url = ''.join(["https://www.townscript.com/",event.div.a.get('href')])
    price = event.div.a.div.find('div', class_='card-body overflow-hidden w-full flex flex-wrap flex-col px-4 pb-4 md:px-5 md:pb-5 ng-star-inserted').find('div',class_='flex items-center justify-between footer ng-star-inserted').div.div.div.span.string

    driver.get(url)
    html = (driver.execute_script("return document.documentElement.innerHTML"))
    # driver.quit()

    soup_inner = bs(html, 'lxml')
    temp = soup_inner.find(id='json-ld').text
    temp = temp[1:]
    temp = temp[:-1]
    json_object = json.loads(temp)
    desc = json_object['description']
    start_date = json_object['startDate']
    end_date = json_object['endDate']
    type = json_object['@type']
    performer = json_object['performer']['name']


    # Given date-time string
    date_str1 = start_date
    date_str2 = end_date

    # Parse the date-time string to a datetime object
    utc_time1 = datetime.strptime(date_str1, '%Y-%m-%dT%H:%M:%S.%f%z')
    utc_time2 = datetime.strptime(date_str2, '%Y-%m-%dT%H:%M:%S.%f%z')

    # Define the IST timezone
    ist = pytz.timezone('Asia/Kolkata')

    # Convert the UTC datetime object to IST
    ist_time1 = utc_time1.astimezone(ist)
    ist_time2 = utc_time2.astimezone(ist)

    # Print the IST datetime
    start = ist_time1.strftime('%H:%M')
    end = ist_time2.strftime('%H:%M')
    schedule = str(start)+'-'+str(end)

    print("Event name :",event_name)
    print("Event date :",event_date)
    print("Location :",location)
    print("URL :",url)
    print("Description: ",desc.rstrip())
    print("Performer: ",performer)
    print("Schedule: ",schedule)
    print("Price :",price)
    print("Category: ", type)

    print("\n\n\n")
    dict_temp['Event Name'] = event_name
    dict_temp['Event date'] = event_date
    dict_temp['Location'] = location
    dict_temp['URL'] = url
    dict_temp['Description'] = desc.rstrip()
    dict_temp['Performer'] = performer
    dict_temp['Schedule'] = schedule
    dict_temp['Price'] = price
    dict_temp['Category'] = type

    t = 'Event '+str(i)
    dict[t] = dict_temp
    i+=1
    driver.refresh()

with open('output.json', 'w') as f:
    json.dump(dict, f)
