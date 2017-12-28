import os  
import selenium
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime
import time
import pandas as pd
import numpy as np

def download_data():

    stock_list = pd.read_txt('C:/stoxx/raw_list.csv', sep=';', usecols=[0])
    stock_list = stock_list.as_matrix()

    chrome_options = Options()  
    chrome_options.add_argument("--headless")  

    mydriver = webdriver.Chrome(executable_path=os.path.abspath('C:/toolkits/chromedriver/chromedriver.exe'), chrome_options=chrome_options)

    start_year = '2000'
    start_month = '01'
    start_day = '01'

    start_date = start_year +'-'+ start_month +'-'+ start_day

    xpaths = []

    end_year = str(datetime.datetime.now().year)
    end_day = str(datetime.datetime.now().day-1)
    end_month = str(datetime.datetime.now().month)

    if datetime.datetime.now().day-1 < 10: end_day = '0' + end_day
    if datetime.datetime.now().month < 10: end_month = '0'+ end_month

    end_date = end_year +'-'+ end_month +'-'+ end_day

    xpaths.append('//*[@id="instSearchHistorical"]')
    xpaths.append('//*[@id="FromDate"]')
    xpaths.append('//*[@id="ToDate"]')

    xpaths.append('//*[@id="exportExcel"]')

    mydriver.get('http://www.nasdaqomxnordic.com/aktier/historiskakurser')
    time.sleep(2)

    i = 0

    for name in stock_list:
        
        mydriver.find_element_by_xpath('//*[@id="instSearchHistorical"]').send_keys(name)
        time.sleep(1)

        mydriver.find_element_by_xpath('//*[@id="instSearchHistorical"]').send_keys(Keys.ARROW_DOWN)    
        time.sleep(1)
        
        mydriver.find_element_by_xpath('//*[@id="instSearchHistorical"]').send_keys(Keys.ENTER)
        time.sleep(1)
        
        mydriver.find_element_by_xpath('//*[@id="FromDate"]').clear()
        time.sleep(1)
        
        mydriver.find_element_by_xpath('//*[@id="FromDate"]').send_keys(start_date)
        time.sleep(1)
        
        mydriver.find_element_by_xpath('//*[@id="ToDate"]').clear()
        time.sleep(1)
        
        mydriver.find_element_by_xpath('//*[@id="ToDate"]').send_keys(end_date)
        mydriver.find_element_by_xpath('//*[@id="ToDate"]').send_keys(Keys.TAB)
        time.sleep(2)

        mydriver.find_element_by_xpath('//*[@id="exportExcel"]').click()
        time.sleep(5)
        
        print (name)

        i = i + 1
        
    mydriver.close()

    print ('Data is downloaded')
    
    return None
    
download_data()
