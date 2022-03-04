from selenium import webdriver
import warnings

warnings.simplefilter("ignore")

driver = webdriver.Chrome()
driver.get("https://www.codewars.com/")

login_btn = driver.find_element_by_xpath('//*[@id="header_section"]/ul/li[3]/a')
login_btn.click()

box_email = driver.find_element_by_xpath('//*[@id="user_email"]')
box_password = driver.find_element_by_xpath('//*[@id="user_password"]')
btn_submit = driver.find_element_by_xpath('//*[@id="new_user"]/button[2]')

user_email = ''
user_password = ''
user_nickname = ''

box_email.send_keys(user_email)
box_password.send_keys(user_password)

btn_submit.click()

# invalid_form_data = driver.find_element_by_xpath('//*[@id="flash"]/div/div/div')

# if invalid_form_data:
#     pass

default_url = driver.current_url
path_start = 'completed_solutions'

driver.get('{0}/{1}/{2}'.format(default_url, user_nickname, path_start))

solutions = driver.find_element_by_xpath('//*[@id="shell_content"]/div[5]/div/div[2]/div')

total_solutions = driver.find_element_by_xpath('//*[@id="shell_content"]/div[5]/div/div[1]/ul/li[1]/a').text

# regex: 'Completed (308)'


driver.close()