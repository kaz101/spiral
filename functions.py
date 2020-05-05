#! /usr/bin/env python3

import selenium
from selenium import webdriver
import time
from random import randrange
from selenium.webdriver.common.keys import Keys


def load_page(links):
    try:
        return links[randrange(len(links))]
    except ValueError:
        return

def get_links( driver):
    elements = driver.find_elements_by_xpath('//a')
    links = []
    for i in elements:
        link = i.get_attribute('href')
        if link and 'google' not in link:
            links.append(link)
    return links

def search_google_images(search ,driver):
    driver.get('https://images.google.com')
    search_box = driver.find_element_by_xpath('//input[@title="Search"]')
    search_box.send_keys(search + Keys.RETURN)
    for i in range(8):
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        try:
            driver.find_element_by_xpath('//input[@value="Show more results"]').click()
        except:
            pass
        time.sleep(.4)
    list = get_links(driver)
    print(len(list))
    return driver, list
