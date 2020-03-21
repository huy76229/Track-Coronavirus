# -*- coding: utf-8 -*-
"""Track Coronavirus Project-------------------------------------------------------------
   Reference Link: https://towardsdatascience.com/how-to-track-coronavirus-with-python-a5320b778c8e
   Data Website: https://www.worldometers.info/coronavirus/
   Date: 2020/03/21
"""
from selenium import webdriver
from time import sleep
import re
from datetime import datetime
import smtplib

country_name = 'S. Korea'

class Coronavirus():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="C:/Users/huy76/Downloads/chromedriver_win32/chromedriver.exe")

    def get_data(self):
        try:

            self.driver.get('https://www.worldometers.info/coronavirus/')
            table = self.driver.find_element_by_xpath('//*[@id="main_table_countries_today"]/tbody[1]')            
            country_element = table.find_element_by_xpath("//td[contains(., '%s')]" % country_name)
            row = country_element.find_element_by_xpath("./..")
            data = row.text.split(" ")

            idx_offset = len(country_name.split(" ")) - 1

            total_cases = data[idx_offset + 1]
            new_cases = data[idx_offset + 2]
            total_deaths = data[idx_offset + 3]
            new_deaths = data[idx_offset + 4]
            active_cases = data[idx_offset + 5]
            total_recovered = data[idx_offset + 6]
            serious_critical = data[idx_offset + 7]

            updated_time = self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div/div[2]")

            print(updated_time.text)
            print("Country: " + country_element.text)
            print("Total cases: " + total_cases)
            print("New cases: " + new_cases)
            print("Total deaths: " + total_deaths)
            print("New deaths: " + new_deaths)
            print("Active cases: " + active_cases)
            print("Total recovered: " + total_recovered)
            print("Serious, critical cases: " + serious_critical)

            self.driver.close()
        except:
            self.driver.quit()

if __name__ == "__main__":
    bot = Coronavirus()
    bot.get_data()