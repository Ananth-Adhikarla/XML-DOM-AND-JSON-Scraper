import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Firefox, FirefoxProfile
import csv

url = "http://www.boxofficemojo.com/studio/"
driver = webdriver.Firefox()
driver.wait = WebDriverWait(driver, 5)
something = []
def looping_pages():

	driver.get("http://dev.markitondemand.com/MODApis/Api/v2/doc")
	link1 = driver.find_element_by_xpath('/html/body/div[4]/div[1]/code')
	link2 = driver.find_element_by_xpath('/html/body/div[4]/div[2]/code')
	link3 = driver.find_element_by_xpath('/html/body/div[4]/div[3]/code')
	link4 = driver.find_element_by_xpath('/html/body/div[4]/div[4]/code')
	link5 = driver.find_element_by_xpath('/html/body/div[4]/div[5]/code')
	link6 = driver.find_element_by_xpath('/html/body/div[4]/div[6]/code')
	
	something.append(link1.text.split("\n"))
	something.append(link2.text.split("\n"))
	something.append(link3.text.split("\n"))
	something.append(link4.text.split("\n"))
	something.append(link5.text.split("\n"))
	something.append(link6.text.split("\n"))
	print(something)
	
	time.sleep(5)


def creating_list(text):

	print(text)	
	for j in text:
		m = j[0].split(" ")
		if( len(m) == 6 ):
			print(m)
			movie_text.append(m)		
		if( len(m) == 7):
			m[1] = m[1]+' '+m[2]
			m[2] = m[3]
			m[3] = m[4]
			m[4] = m[5]
			m[5] = m[6]
			del m[6]
			print(m)
			movie_text.append(m)
		if( len(m) == 8):
			m[1] = m[1]+' '+m[2]+' '+m[3]
			m[2] = m[4]
			m[3] = m[5]
			m[4] = m[6]
			del m[5]
			del m[6]
			print(m)
			movie_text.append(m)
						
		
	return movie_text

def write_to_csv():

	count = 0
	with open('Box_office_selenium.csv', 'a+') as csvfile:
		
		writer = csv.writer(csvfile)
	
		for i,j in enumerate(movie_text):
			count += 1
			writer.writerow(j)
			
		writer.writerow(" ")

	print("Total number of records processed : ",count)

looping_pages()
#creating_list(x)
#write_to_csv()

