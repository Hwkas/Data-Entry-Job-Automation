# Data-Entry-Job-Automation
This project is about scraping data from 'https://www.99acres.com' about all the properties up for rent.
After appling the desired filters, get the deatils of the property and save that data into a .csv fle.
Technology/Packages used :- Python, Selenium, BeautifulSoup, Pandas
The way this program works is that 
* first selenium opens up the websiter, then apply filters for teh property
* Then is fethes the url/link of all those propersites
* Then beautifulsoup in is used to get the details about the individaul properties, like - rent, bhk, type, address, ulr/link.
* Then all those deatials a saved into a .csv file using pandas.
