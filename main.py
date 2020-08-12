import sys
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import pyautogui as pg
import pandas as pd
import csv

#sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

def drive():
    d = webdriver.Chrome('/Users/yo/Desktop/file-python/scraping/chromedriver')
    d.get("https://www.driveplaza.com/dp/SearchTop")        
    return d

def delete(arg):
    pg.hotkey("Command","a")
    #arg.send_keys(Keys.COMMAND,"a")
    arg.send_keys(Keys.DELETE)

def input_ic(arg1,arg2):
    arg1.send_keys("{0}".format(arg2))

def submit(arg1):
    arg1.submit()

def input_csv():
    df = pd.read_csv("ic_list.csv", encoding="shift-jis",header = None).values.tolist()
    ic = sum(df,[])
    ic = [i.replace("インターチェンジ","") for i in ic]
    ic = [i.replace("出入口","") for i in ic]
    ic = [i.replace("出口","") for i in ic]
    ic = [i.replace("入口","") for i in ic]
   
    return ic

# def create_write_file():
#     header = ["基準料金−1","ETC料金−1","ETC料金2.0−1","通常時間-1","渋滞考慮時間-1",\
#             "基準料金−2","ETC料金−2","ETC料金2.0−2","通常時間-2","渋滞考慮時間-2",\
#             "基準料金−3","ETC料金−3","ETC料金2.0−3","通常時間-3","渋滞考慮時間-3",]
#     with open("ic.csv", "a") as file:
#         writer = csv.writer(file, lineterminator="\n")
#         writer.writerow(header)

# def write_csv(cost_list):
#     with open("ic.csv", "a") as file:
#         writer = csv.writer(file, lineterminator="\n")
#         writer.writerow(cost_list)


def main():

    driver = drive()
    #ic = input_csv()

    departure = driver.find_element_by_name("startPlaceKana")    
#    input_ic(departure,"{0}".format(ic[0]))
    input_ic(departure,"柏")

    arrival = driver.find_element_by_name("arrivePlaceKana")
    input_ic(arrival,"仙台南")
    submit(arrival)

    sleep(3)

    cost_list = []
    cost = driver.find_elements_by_xpath("//span[@class='cell']")
    for span in cost:
        print(span.text)  
        cost_list.append(span.text)
        
    dist_list = []
    distance = driver.find_elements_by_xpath("//span[@class='cell distance']")
    for span in distance:
        print(span.text)
        dist_list.append(span.text)

    sleep(5)
    driver.close()

if __name__ == "__main__":
    main()