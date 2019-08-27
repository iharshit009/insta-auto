from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.action_chains import ActionChains


browserProfile = webdriver.ChromeOptions()
browser = webdriver.Chrome("chromedriver.exe")
email = ""
password = ""

browser.get('https://www.instagram.com/accounts/login/')

emailInput = browser.find_elements_by_css_selector('form input')[0]
passwordInput = browser.find_elements_by_css_selector('form input')[1]

emailInput.send_keys(email)
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.ENTER)
time.sleep(2)

browser.get('https://www.instagram.com/include._')
followersLink = browser.find_element_by_css_selector('ul li a')
followersLink.click()
time.sleep(2)
followersList = browser.find_element_by_css_selector('div[role=\'dialog\'] ul')
numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

followersList.click()
actionChain = webdriver.ActionChains(browser)
ActionChains(webdriver).move_to_element(webdriver.find_elements_by_tag_name('button')).click().perform()
while (numberOfFollowersInList < 1500):
    actionChain.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
    numberOfFollowersInList = len(followersList.find_elements_by_css_selector('li'))

followers = []
for user in followersList.find_elements_by_css_selector('li'):
    userLink = user.find_element_by_css_selector('a').get_attribute('href')
    print(userLink)
    followers.append(userLink)
    if (len(followers) == 1500):
        break
    else:
        print("lst line")
