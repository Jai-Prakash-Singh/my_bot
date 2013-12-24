#!/usr/bin/env python

from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.proxy import *
#from pyvirtualdisplay import Display
from random import choice



ip_list = ['69.175.58.62:80', '108.178.5.194:80', '165.231.12.159:80', '173.0.62.153:80', '165.231.12.161:80', '196.196.18.155:80', '173.0.53.53:80', '165.231.12.164:80', '173.236.45.86:80', '184.154.129.156:80', '165.231.12.158:80', '66.248.193.115:80', '173.232.104.225:80', '173.236.28.76:80', '173.232.104.27:80', '196.196.18.153:80', '196.196.18.150:80', '173.213.99.151:80', '165.231.12.160:80', '173.0.56.46:80', '173.236.50.205:80', '173.213.98.178:80', '173.213.99.162:80', '173.232.104.228:80', '108.178.25.197:80', '196.196.18.147:80', '66.248.193.140:80', '173.236.45.84:80', '196.196.18.15:80', '176.61.140.250:80', '184.154.129.157:80', '173.0.62.148:80', '165.231.12.165:80', '196.196.18.152:80', '209.148.92.64:80', '173.0.59.136:80', '173.236.56.90:80', '173.236.56.30:80', '165.231.12.157:80', '199.180.134.207:80', '173.0.56.16:80', '173.212.192.132:80', '184.154.10.140:80', '108.163.234.134:80', '173.236.45.85:80', '173.232.104.252:80', '196.196.18.148:80', '184.154.129.238:80', '94.23.76.190:80', '66.248.193.132:80', '184.154.104.150:80', '173.236.71.189:80', '165.231.12.162:80', '66.248.193.12:80', '184.154.119.130:80', '173.0.53.54:80', '5.153.237.34:80', '91.108.183.114:80', '184.154.105.117:80', '184.154.119.226:80', '173.0.48.37:80', '184.154.129.235:80', '196.196.18.154:80', '173.236.56.26:80', '184.154.116.126:80', '173.0.56.42:80', '173.0.54.64:80', '184.154.115.3:80', '196.196.18.156:80', '173.232.104.229:80', '66.248.193.106:80', '173.0.52.160:80', '173.0.56.105:80', '174.140.169.142:80', '69.175.58.59:80', '165.231.12.16:80', '173.0.53.55:80', '173.236.28.77:80', '66.248.193.136:80', '66.248.193.152:80', '173.254.204.248:80', '184.154.133.147:80', '184.154.129.158:80', '173.232.104.134:80', '173.232.107.163:80', '173.0.59.201:80', '173.236.50.206:80', '66.248.193.144:80', '185.3.134.98:80', '173.232.104.136:80', '66.248.193.113:80', '165.231.12.166:80', '173.236.50.203:80', '173.0.59.177:80', '173.0.57.206:80', '174.140.169.14:80', '173.0.52.49:80', '69.175.58.60:80', '66.248.193.137:80', '173.0.56.38:80']



#https://getfirebug.com/releases/firebug/1.11/

def main(link):
    #display = Display(visible=0, size=(800, 600))
    #display.start()
    ip_port = choice(ip_list)
    myProxy = 'http://vinku:india123@'+ip_port
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myProxy,
        'ftpProxy': myProxy,
        'sslProxy': myProxy,
        'noProxy': '' # set this value as desired
        })

    #driver = webdriver.Firefox(proxy=proxy)
    fp = webdriver.FirefoxProfile()
    file = "/home/user/.mozilla/firefox/41bljqjm.default/extensions/firebug@software.joehewitt.com.xpi"
    fp.add_extension(extension=file)
    fp.set_preference("extensions.firebug.currentVersion", "1.11.2")
    browser = webdriver.Firefox(firefox_profile=fp,proxy=proxy)
    #browser.get("http://goarticles.com/register.html")
    browser.get(link)
    html_source = browser.page_source
    return html_source,browser

if __name__=="__main__":
    link = "http://goarticles.com/"
    page = main(link)
    print page 



