#!/usr/bin/env python 
# -*- coding: latin-1 -*-
# -*- coding: iso-8859-15 -*-
# -*- coding: ascii -*-
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import firebug_proxy2
import time
from selenium.webdriver.support.ui import Select



def login():
    #driver = webdriver.Firefox()
    link = "http://goarticles.com/members/"
    driver = firebug_proxy2.main(link)
    #driver.get(link)
    elem = driver.find_element_by_name("email")
    elem.send_keys("kayakashyap213@gmail.com")
    elem = driver.find_element_by_name("password")
    elem.send_keys("playboy")
    elem.send_keys(Keys.RETURN)
    #dir(driver)
    elem = driver.find_element_by_id("add_new")
    elem.send_keys(Keys.RETURN)
    select = Select(driver.find_element_by_name('category_id'))
    
    select.select_by_index(2)
    #select = Select(driver.find_element_by_name('sub_category_id'))
    #select.select_by_index(1)
    elem = driver.find_element_by_name("title")
    title  = "Different Ways You Can Define Yourself  "
    elem.send_keys(title)
    f = open("f1.html")
    body = f.read()
    body = unicode(body, errors='ignore')
    f.close()
    elem = driver.find_element_by_name("body")
    elem.send_keys(body)
    bio =" name  Kaya, just learing how to write a article"
    elem = driver.find_element_by_name("resource")
    elem.send_keys(bio)
    elem = driver.find_element_by_name("submit").click()
    #elem.submit() 
    time.sleep(5)
    driver.close()


if __name__=="__main__":
    login()

