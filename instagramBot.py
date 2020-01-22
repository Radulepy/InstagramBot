#----------------------------
#							|
# Instagram Bot - Lepy					|
# learn.lepystudio.ro					|
#							|
#----------------------------

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
import string

#Change this list to your wanted comments
comments = [' I am a robotttt', 'Nice ', 'loool very nice! ', 'I like it!', 'Super ;) ', 'hmmm, interesting ', ' hi', 'I am a sheep ', 'learn something new ', 'Mind blowing ', 'I like to eat wires', ]

#This are some variables to keep tracking of the posts
posts=0

#Chromedriver path. Make sure to have the same Chromedriver version as your Google Chrome browser
browser = webdriver.Chrome(executable_path=r "C:\Users\Lepy\Name\python\chromedriver.exe")  # <----- ENTER PATH HERE 

browser.get(('https://www.instagram.com/accounts/login/?source=auth_switcher'))
sleep(2) 
	

def likeAndComm(): # Likes and Comments the first 9 posts
	global posts
	for y in range (1,4):
		for x in range(1,4):
			post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div[1]/div/div['+str(y)+']/div['+str(x)+']') 
			browser.implicitly_wait(1) 
			post.click()
			sleep(2)
			postLike = browser.find_element_by_class_name('wpO6b') 
			postLike.click() 
			sleep(2)
			comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click() 
			sleep(3)
			comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click() 
			comment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(random.choice(comments))	
			sleep(3)
			sendComment = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button') 
			sendComment.click()
			sleep(2)
			posts+=1
			closePost=browser.find_element_by_xpath('/html/body/div[4]/button[1]')
			closePost.click()
			sleep(3)
		print ('Nr. of posts: ' +str(posts))
	
	sleep(5)
	browser.get('https://www.instagram.com/explore/')
	sleep(6)
	likeAndComm()
	
		
def start():
	#browser.implicitly_wait(3)  #this is another wait function.If you would like to run the script faster, change all sleep() to this
	username = browser.find_element_by_name('username')
	username.send_keys('instagramUsername') # <- INSERT YOUR INSTAGRAM USERNAME HERE -------------------------------------------------------------------------------------------------------------------------
	password = browser.find_element_by_name('password')
	password.send_keys('instagramPassword') # <- INSERT YOUR INSTAGRAM PASSWORD HERE -----------------------------------------------------------------------------------------------------------------------
	nextButton = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
	nextButton.click()
	#browser.quit()
	sleep(4)
	notification = browser.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
	notification.click()
	browser.get('https://www.instagram.com/explore/')
	sleep(6)
	likeAndComm() # likeAndComm function ----------------------------------------------------------------------------------------------------------------------------------------------------------
	#post = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div[1]/div/div[1]/div[2]')
	#post.click()
	sleep(5)
	
	
#Start the programm
start()
