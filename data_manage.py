import requests
from bs4 import BeautifulSoup
import pandas


class DataManager:
    """This class is responsible for managing all the data."""

    def __init__(self):
        self.prop_details_dict = {}
        # function
        self.beautifulsoup_function()
        self.pandas_function()

    def beautifulsoup_function(self):
        """This function uses beautiful soup to get all the need details of the property"""

        # getting all the links from the
        with open(file="links.txt", mode="r") as data:
            properties_links = data.readlines()

        # declaring empty lists
        rent_list = []
        bhk_list = []
        property_type_list = []
        address_list = []

        for link in properties_links:
            # ------------------------------------------- BeautifulSoup----------------------------------- #

            # using requests package to get download the webpage.
            response = requests.get(url=link)
            response.raise_for_status()
            web_data = response.text

            # using beautiful soup to fetch the details about the property
            soup = BeautifulSoup(web_data, "html.parser")
            # getting rent of the property
            rent = soup.find(id="pdPrice").get_text(strip=True)
            rent_list.append(rent)
            # print(rent)

            # we don't need BHK as i already have added BHK filter in website
            bhk = soup.find(id="bedWash").get_text()
            bhk_list.append(bhk)
            # print(bhk)

            # getting property type
            property_type = soup.find(id="headerDescription").get_text()
            property_type_list.append(property_type)
            # print(property_type)

            # getting address
            address = (soup.find(name="span", class_="component__pdPropAddress").get_text(strip=True)[3:]).split(",")[
                      0:2]
            address = str(address[0] + address[1])
            address_list.append(address)
            # print(address)

        self.prop_details_dict = {"Rent (₹)": rent_list, "BHK": bhk_list, "Property Type": property_type_list,
                                  "Address": address_list, "URL": properties_links}

    def pandas_function(self):
        """Using pandas library to save the property data into a csv file."""
        df = pandas.DataFrame.from_dict(self.prop_details_dict)
        df.sort_values(by="Rent (₹)", inplace=True)
        df.reset_index(inplace=True, drop=True)
        df.to_csv("property_data.csv")
