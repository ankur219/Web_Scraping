from selenium import webdriver
from selenium.webdriver.common.keys import Keys

co=webdriver.ChromeOptions()
path_to_chromedriver = 'C:/Python35-32/chromedriver'
co.arguments.append('--user-agent=MSIE')
browser = webdriver.Chrome(executable_path = path_to_chromedriver,chrome_options=co)

browser.get('http://oars.cc.iitk.ac.in:6060/')

browser.switch_to_default_content()
browser.switch_to_frame('menu')
browser.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/span[2]/a/b').click()
browser.find_element_by_xpath('//*[@id="t_treeid_60"]/span[1]/a/b').click()


browser.switch_to_default_content()
browser.switch_to_frame(browser.find_element_by_xpath('/html/frameset/frameset/frame[2]'))
username =browser.find_element_by_name('LoginID')
username.send_keys(input())


browser.switch_to_default_content()
browser.switch_to_frame(browser.find_element_by_xpath('/html/frameset/frameset/frame[2]'))
password =browser.find_element_by_name('Password')
password.send_keys(raw_input())

browser.find_element_by_xpath('//*[@id="loginFrom"]').click()

alert=browser.switch_to_alert()
alert.accept()

browser.switch_to_default_content()
browser.switch_to_frame('menu')
browser.find_element_by_tag_name('b').click()
browser.find_element_by_xpath('/html/body/table/tbody/tr/td/table/tbody/tr/td/span[4]/a/b').click()
browser.find_element_by_xpath('//*[@id="t_treeid_95"]/span[6]/a/b').click()

browser.switch_to_default_content()
browser.switch_to_frame('main')
browser.find_element_by_xpath('/html/body/font/center/b/font/a').click()


y=browser.find_elements_by_tag_name('td')
a=[]
for i in y:
	a.append(i.text)






mondayDict_M={}
time1=8
for i in range (14,25):
   if int(time1) == time1:
     mondayDict_M[str(time1) + ":00"] = a[i]
   else:
     mondayDict_M[str(int(time1)) + ":30"] = a[i]
   time1 += 0.5

tuesdayDict_M={}
time1=8
for i in range (26,37):
   if int(time1) == time1:
     tuesdayDict_M[str(time1) + ":00"] = a[i]
   else:
     tuesdayDict_M[str(int(time1)) + ":30"] = a[i]
   time1 += 0.5

wednesdayDict_M={}
time1=8
for i in range (38,49):
   if int(time1) == time1:
     wednesdayDict_M[str(time1) + ":00"] = a[i]
   else:
     wednesdayDict_M[str(int(time1)) + ":30"] = a[i]
   time1 += 0.5


thursdayDict_M={}
time1=8
for i in range (50,61):
   if int(time1) == time1:
     thursdayDict_M[str(time1) + ":00"] = a[i]
   else:
     thursdayDict_M[str(int(time1)) + ":30"] = a[i]
   time1 += 0.5

fridayDict_M={}
time1=8
for i in range (62,73):
   if int(time1) == time1:
     fridayDict_M[str(time1) + ":00"] = a[i]
   else:
     fridayDict_M[str(int(time1)) + ":30"] = a[i]
   time1 += 0.5


mondayDict_E={}
time1=14
for i in range (85,95):
   if int(time1) == time1:
     mondayDict_E[str(time1) + ":00"] = a[i]
   else:
     mondayDict_E[str(int(time1)) + ":30"] = a[i]
   time1 += 0.5

tuesdayDict_E={}
time1=14
for i in range (96,106):
   if int(time1) == time1:
     tuesdayDict_E[str(time1) + ":00"] = a[i]
   else:
     tuesdayDict_E[str(int(time1)) + ":30"] = a[i]
   time1 += 0.5

wednesdayDict_E={}
time1=14
for i in range (107,117):
   if int(time1) == time1:
     wednesdayDict_E[str(time1) + ":00"] = a[i]
   else:
     wednesdayDict_E[str(int(time1)) + ":30"] = a[i]
   time1 += 0.5

thursdayDict_E={}
time1=14
for i in range (118,128):
   if int(time1) == time1:
     thursdayDict_E[str(time1) + ":00"] = a[i]
   else:
     thursdayDict_E[str(int(time1)) + ":30"] = a[i]
   time1 += 0.5

fridayDict_E={}
time1=14
for i in range (129,139):
   if int(time1) == time1:
     fridayDict_E[str(time1) + ":00"] = a[i]
   else:
     fridayDict_E[str(int(time1)) + ":30"] = a[i]
   time1 += 0.5


DICT ={}
DICT.update(mondayDict_M)
DICT.update(tuesdayDict_M)
DICT.update(wednesdayDict_M)
DICT.update(thursdayDict_M)
DICT.update(fridayDict_M)
DICT.update(mondayDict_E)
DICT.update(tuesdayDict_E)
DICT.update(wednesdayDict_E)
DICT.update(thursdayDict_E)
DICT.update(fridayDict_E)

print (DICT) 
