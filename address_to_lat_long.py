from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

address_file = open('./addresses.txt', 'r')
outfile = open('station_coordinates.txt', 'w')

address_file.readline()

geoBlocked = webdriver.FirefoxOptions()
geoBlocked.set_preference("geo.prompt.testing", True)
geoBlocked.set_preference("geo.prompt.testing.allow", False)

driver = webdriver.Firefox(options=geoBlocked)
driver.get("https://www.gps-coordinates.net/")

for line in address_file.readlines():
    if line != "name":
        time.sleep(1)
        input_bar = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/form[1]/div[1]/div/input")
        input_bar.clear()
        input_bar.send_keys(line)
        driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/form[1]/div[2]/div/button").click()
        time.sleep(0.2)
        lat_long_bar = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[3]/div[1]/form[2]/div[4]/div/input")
        outstring = line[:-2]
        outstring += ';' + lat_long_bar.get_attribute('value') + '\n'
        outfile.write(outstring)

outfile.close()
address_file.close()
        