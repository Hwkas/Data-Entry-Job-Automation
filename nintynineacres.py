from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep


class NinetyNineAcres:
    """Here in this class selenium is used to fetch the links for all the desired properties."""

    def __init__(self, chrome_driver_path, mb_url):
        """here we are creating a selenium object"""
        service_obj = Service(executable_path=chrome_driver_path)
        self.driver = webdriver.Chrome(service=service_obj)
        self.driver.get(url=mb_url)
        self.config()
        self.prop_link()

    def config(self):
        """its filter the search in the website"""
        sleep(2)
        max_budget_btn = self.driver.find_element(By.XPATH, '//*[@id="bdf__lf_budMax"]').click()
        max_budget_value_btn = self.driver.find_element(By.XPATH, '//*[@id="lf_budget_max_list"]/li[35]').click()
        sleep(0.5)
        no_of_room = self.driver.find_element(By.XPATH,
                                              '/html/body/div[1]/div/div/div[4]/div[2]/section/div/div[4]/div/div/div[2]/div[2]').click()
        sleep(0.5)
        verifie_prop_toogle = self.driver.find_element(By.XPATH, '//*[@id="verified"]/span/label').click()

    def prop_link(self):
        """here we are getting the property link, returns the list of all the links"""
        sleep(1)
        links = self.driver.find_elements(By.CSS_SELECTOR, "tr td a")
        # here it is providing two pages(links) for a single property, one for rent and to sale.
        # to filter out the for buy property links, i am trying to convert the first character after
        # the link 'https://www.99acres.com/' into int if it converts into int then it's a for rent link
        # other-wise it's for sale link.
        # examples for rent - 'https://www.99acres.com/2-bhk-bedroom-apartment-flat-for-rent-in-m3m-sierra-68-sector-68-gurgaon-1450-sq-ft-r2-spid-D57515916'
        # in the above link it's mostly 2 because i filtered out the 2 BHK flats.
        # example for sale - 'https://www.99acres.com/m3m-sierra-68-sector-68-gurgaon-npxid-r211327'
        # list to store the links in list.
        links_list = []
        for l in links:
            try:
                i = int(l.get_attribute("href")[24])
                # print(l.get_attribute("href"))
                # here adding new line to write the links in a proper format in the file 'links.txt'
                links_list.append(f'{l.get_attribute("href")}\n')
            except:
                pass
        # writing all the links into the file.
        with open(file="links.txt", mode="w") as data:
            data.writelines(links_list)
