from selenium import webdriver

#loding the driver for browser we want to interact
##for chrome on windows 
#driver = webdriver.Chrome(executable_path=r'C:\Users\zfdj2646\Downloads\chromedriver.exe')

user = input('Enter User Name :')

try: 
    password = getpass.getpass() 
except Exception as error: 
    print('ERROR', error)

## for firefox on ubuntu
driver = webdriver.Firefox(executable_path=r'/home/sardarkhan/Desktop/Projects/auto-email/geckodriver-v0.26.0-linux64')

##similarly on can do it for other browswer by providing the corresponding driver detail by following below code
##driver = webdriver.Browser(executable_path=r'driver/path/needs/to/be/pasted/in/this/single/quotes')


#getting the link for the website we want to work on
driver.get("https://www.gmail.com")

#a decent time delay to load the website and fake human interaction
driver.implicitly_wait(60)

#fetching the html id to send email-address to sign-in
emailElem = driver.find_element_by_id('identifierId')
emailElem.send_keys(user)

driver.implicitly_wait(60)
nextButton = driver.find_element_by_id("identifierNext").click()
driver.implicitly_wait(60)

#fetching the html id to send password to sign-in
passwordElem = driver.find_element_by_id('password')
passwordElem.send_keys(password)

signinButton = driver.find_element_by_id('signIn')
signinButton.click()