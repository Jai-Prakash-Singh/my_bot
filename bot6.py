#!/usr/bin/enc python 

from selenium import *
from selenium.webdriver.common.keys import *
from selenium.webdriver.support.ui import Select
import mechanize
import sys
import webbrowser
from bs4 import BeautifulSoup
import re
import br_proxies
import firebug_proxy


def main3(fpage,driver,captcha,form):
    for control in form.controls:
      if str(control.type) == "text" and str(control.name) =="email":
          e =str(control.name)
          elem = driver.find_element_by_name(e)
          elem.send_keys("jp213@ymail.com")
      elif str(control.type)=="text":
          t =str(control.name)
          elem = driver.find_element_by_name(t)
          elem.send_keys("kaya kashyap")
      elif str(control.type) =="select":
          s =str(control.name)
          select = Select(driver.find_element_by_name(s))
          select.select_by_visible_text("India")
      elif str(control.type) =="password":
          p =str(control.name)
          elem = driver.find_element_by_name(p)
          elem.send_keys("playboy13")
      elif str(control.type)=="checkbox":
          c =str(control.name)
          elem = driver.find_element_by_name(c)
          #if not elem.isSelected():
          elem.click()
      elif re.search(r"captcha",str(control.name)):
          cp =str(control.name)
          elem = driver.find_element_by_name(cp)
          elem.send_keys(captcha)
      elif str(control.type)=="submit":
         sb =str(control.name) 
         driver.find_element_by_name(sb).click()
      
      print driver.title


def main2(url,fpage,driver,captcha):
    '''request = mechanize.Request(url)
    request.set_proxy('218.103.8.66:8080',"http")
    response = mechanize.urlopen(request)
    forms = mechanize.ParseResponse(response, backwards_compat=False)
    response.close()'''
    br = mechanize.Browser()
    br.set_handle_robots(False)   # ignore robots
    br.set_handle_refresh(False)  # can sometimes hang without this
    br.addheaders =[('User-agent', 'Firefox')]
    #br_proxies.main(br)
    response = br.open(url)
    br.form = list(br.forms())[1]
    main3(fpage,driver,captcha, br.form)

    
def main():
    url = "http://goarticles.com/register.html"
    fpage,driver = firebug_proxy.main(url)
    print driver.title
    soup = BeautifulSoup(fpage)
    data = soup.find_all("div",attrs={"id":"recaptcha_image"})
    for l in data:
        image = str(l.img["src"])

    webbrowser.open(image)
    captcha  = raw_input("enter the captcha: ")
    main2(url,fpage,driver,captcha)
 



if __name__=="__main__":
    main()
   
