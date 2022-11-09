import selenium
from  selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.keys import Keys
import csv
from selenium.webdriver.common.by import By

with open('tweets.csv', mode='w',encoding="utf-8") as csv_file:
      fieldnames = ['tweet', 'statu']
      writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
      writer.writeheader()

      kullanici = input("Kullanıcı adı giriniz :")
      sifre = input("Şifre giriniz :")
      profil = input("Analizi yapılacak kişinin profil adresini giriniz :")

      options = Options()
      options.binary_location="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

      driver_path = "C:\\Users\\fatihocal\\Downloads\\chromedriver.exe"
      browser = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
      browser.get("https://twitter.com")

      time.sleep(2)

      browser.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/div[5]/a/div').click()
      time.sleep(2)
      # fill the number or mail
      browser.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input').send_keys(kullanici)
      time.sleep(2)
      browser.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div').click()
      time.sleep(2)
      # fill the password
      browser.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(sifre)
      
      # clicking on that element 
      time.sleep(2)
      browser.find_element_by_xpath('//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div').click()
      time.sleep(2)


      browser.get("https://twitter.com/"+profil)

      body = browser.find_element_by_tag_name('body')
      for _ in range(10): #kaç tweet gelecek.
         body.send_keys(Keys.PAGE_DOWN)
         time.sleep(0.2)

      tweets = browser.find_elements_by_css_selector("[data-testid=\"tweet\"]")
      # tweets = browser.find_elements_by_css_selector('.css-901oao.r-18jsvk2.r-1qd0xha.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0 span')

      for tweet in tweets:
            print("-----------")
            print(tweet.text) 
            print("-----------")
        
            writer.writerow({'tweet': tweet.text.replace(',','')})
         # writer.writerow({'tweet': tweet.text.replace('\n','')})