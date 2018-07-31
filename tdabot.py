from selenium import webdriver  
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time


question1 = input('Enter any key to strat the TDA BOT   ').lower()

q = str(question1)
print(len(q))

if len(q) >= 0:
    
    def one_hour():
        options = webdriver.ChromeOptions()
                            
        options.add_argument("-headless")
        driver = webdriver.Chrome(chrome_options=options)
        #driver = webdriver.Chrome()

        driver.get('https://www.genbook.com/bookings/slot/reservation/30011361/1135179/-1?bookingSourceId=1000&category=1135193')
        try:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='error']")))
            

            no_times = driver.find_element_by_xpath("//div[@class='error']")

            print('\n' + no_times.text+ ' (1 hour)\n')
            driver.close()
        except:
            drive_date = driver.find_element_by_xpath("//div[@id='datetime']").text
            drive_time = driver.find_element_by_xpath("//li[@class='timeslot']").text
            driver.close()

            check = drive_date +','+drive_time+'/'
            checker = open('drive.txt', 'r')
            checker1 = checker.read()
            checker.close()

           

            
            if check != checker1:
                print('\nsending emial...\n')
                checker2 = open('drive.txt', 'w')
                checker2.write(check)
                checker2.close()
                
                options = webdriver.ChromeOptions()
                                
                options.add_argument("-headless")
                driver2 = webdriver.Chrome(chrome_options=options)
                #driver2 = webdriver.Chrome()
                timeout = 15
                #go to gmail.com
                driver2.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
                soup = driver2.page_source
                #WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='Xb9hP']")))
                #this is where you enter email address
                WebDriverWait(driver2, 60).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='Xb9hP']")))
                textbox = driver2.find_element_by_xpath("//div[@class='Xb9hP']")
                #ths is the "Next" button to get to the page where you type the password
                next_btn = driver2.find_element_by_xpath("//div[@id='identifierNext']")
                #sends email adress info
                textbox.send_keys(*******) #Change this for your own email
                #clicks next
                next_btn.click()
                time.sleep(5)
                textbox2 = driver2.find_element_by_xpath("//input[@name='password']")
                textbox2.send_keys(******) #Your Passowrd
                next_btn2 = driver2.find_element_by_xpath("//span[@class='RveJvd snByac']")
                next_btn2.click()
                timeout = 20
                WebDriverWait(driver2, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='T-I J-J5-Ji T-I-KE L3']")))
                compose_btn = driver2.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']")
                compose_btn.click()
                time.sleep(3.3)
                email_address = driver2.find_element_by_xpath("//textarea[@class= 'vO']")
                subject_box = driver2.find_element_by_xpath("//input[@name='subjectbox']")
                email_address.send_keys(********) #Change for your own info
                subject_box.send_keys('Drive Time Alert')
                messege_box = driver2.find_element_by_xpath("//div[@class='Am Al editable LW-avf']")
                messege_box.click()
                messege_box.send_keys('Hey, there are 1 hour drive times avaliable... One is '+date+' at '+' time. Go to https://www.genbook.com/bookings/slot/reservation/30011361/1135179/-1?bookingSourceId=1000&category=1135193 to find out more')
                send_btn = driver2.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO T-I-atl L3']")
                send_btn.click()
                time.sleep(8)
                driver2.close()
            else:
                print('\nKnown opening for 1 hour lesson.\n')






    def two_hour():
        options = webdriver.ChromeOptions()
                            
        options.add_argument("-headless")
        driver = webdriver.Chrome(chrome_options=options)
        #driver = webdriver.Chrome()

        driver.get('https://www.genbook.com/bookings/slot/reservation/30011361/1139128/-1?bookingSourceId=1000&category=1135193')
        #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='error']")))
        try:
            WebDriverWait(driver, 15).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='error']")))

            no_times = driver.find_element_by_xpath("//div[@class='error']")
            print('\n' + no_times.text+ ' (2 hour)\n')
            driver.close()
        except:
            drive_date = driver.find_element_by_xpath("//div[@id='datetime']").text
            drive_time = driver.find_element_by_xpath("//li[@class='timeslot']").text
            driver.close()

            check = drive_date +','+drive_time+'/'
            checker = open('drive.txt', 'r')
            checker1 = checker.read()
            checker.close()


            if check != checker1:
                print('\nsending email...\n')
                checker2 = open('drive.txt', 'w')
                checker2.write(check)
                checker2.close()
                options = webdriver.ChromeOptions()
                                
                options.add_argument("-headless")
                driver2 = webdriver.Chrome(chrome_options=options)
                #driver2 = webdriver.Chrome()
                timeout = 15
                #go to gmail.com
                driver2.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
                soup = driver2.page_source
                #WebDriverWait(driver, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='Xb9hP']")))
                #this is where you enter email address
                time.sleep(9)
                textbox = driver2.find_element_by_xpath("//div[@class='Xb9hP']")
                #ths is the "Next" button to get to the page where you type the password
                next_btn = driver2.find_element_by_xpath("//div[@id='identifierNext']")
                #sends email adress info
                textbox.send_keys(********) #Change for your own email
                #clicks next
                next_btn.click()
                time.sleep(5)
                textbox2 = driver2.find_element_by_xpath("//input[@name='password']")
                textbox2.send_keys(******) #Your password
                next_btn2 = driver2.find_element_by_xpath("//span[@class='RveJvd snByac']")
                next_btn2.click()
                timeout = 20
                WebDriverWait(driver2, timeout).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='T-I J-J5-Ji T-I-KE L3']")))
                compose_btn = driver2.find_element_by_xpath("//div[@class='T-I J-J5-Ji T-I-KE L3']")
                compose_btn.click()
                time.sleep(3.3)
                email_address = driver2.find_element_by_xpath("//textarea[@class= 'vO']")
                subject_box = driver2.find_element_by_xpath("//input[@name='subjectbox']")
                email_address.send_keys(*******) #Change for your own email 
                subject_box.send_keys('Drive Time Alert')
                messege_box = driver2.find_element_by_xpath("//div[@class='Am Al editable LW-avf']")
                messege_box.click()
                messege_box.send_keys('Hey, there are 2 hour drive times avaliable. Go to https://www.genbook.com/bookings/slot/reservation/30011361/1135179/-1?bookingSourceId=1000&category=1135193 to find out more')
                send_btn = driver2.find_element_by_xpath("//div[@class='T-I J-J5-Ji aoO T-I-atl L3']")
                send_btn.click()
                time.sleep(8)
                driver2.close()
            else:
                print('\nKnown opening for 2 hour lesson.\n')

    
        
    while True:
        one_hour()
        two_hour()
        for i in [1,2,3,4,5]:
            time.sleep(60)
            print(i, ' minute(s) of 5')
            
