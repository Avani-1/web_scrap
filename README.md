Prerequisites : 
1. Google Chrome
2. Chrome Driver : https://googlechromelabs.github.io/chrome-for-testing/
3. BeautifulSoup Library {To access static data}
4. Selenium {To access JS dependent dynamic data}

Once the requirements have been met, simply run the main.py file.
It will result in the creation of a event_data.json file having the scraped data.
Furthermore, the results will also be displayed on the console.

Note, the assignment uses BeautifulSoup and Selenium at the same time because the the website's dynamic dependency on JS. i.e., it was necessary to mimic human interaction in order to scrape the data. This is where the chrome driver comes in use as well.

The event listing website used is : https://www.townscript.com/

Data Collection Summary -
Format : JSON
Fields : 
    1. Event Name
    2. Event Date
    3. Location
    4. URL
    5. Description : As mentioned by the organizers on the event listing website
    6. Performer : Here, it corresponds the the organizer since the speakers were not explicitly mentioned.
    7. Schedule : In IST 24-hrs clock format
    8. Price : In INR
    9. Category : In accordance teh the event listing website's categorization.
