from nintynineacres import *
from data_manage import *

# constants
CHROME_DRIVER_PATH = "YOUR CHROME DRIVER PATH"
URL = "https://www.99acres.com/property-for-rent-in-gurgaon-ffid"

# creating an object & getting the links for the properties
nintynineacres_obj = NinetyNineAcres(CHROME_DRIVER_PATH, URL)

# creating an object
data = DataManager()
