import time
from selenium import webdriver
from DiscordAccount import DiscordAccount
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from LocalStorage import LocalStorage
from sys import argv
import sys
from selenium.webdriver.common.action_chains import ActionChains

global trys

x = 0
trys = 0

exit_when_done = True
use_saved_email = True
#auto_join = True

invite_code = 'dpy'

useragent = UserAgent(verify_ssl=False)
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": useragent.random})
actions = ActionChains(driver)
print(driver.execute_script("return navigator.userAgent;"))

#def Auto_Join():
 #   auto_join = True
  #  print('Checking login...')
   # if driver.current_url == 'https://discord.com/channels/@me' and auto_join == True:
    #    print('Switching to the discord server...')
     #   driver.execute_script("window.open('https://discord.com/invite/minecraft');")
      #  time.sleep(2)
       # driver.switch_to.window(driver.window_handles[0])
        #time.sleep(0.1)
#        driver.close()
 #       time.sleep(0.1)
  #      driver.switch_to.window(driver.window_handles[0])
   #     time.sleep(15)
    #    Ai = driver.find_element_by_name("Accept Invite")
     #   Ai.click()
      #  print('Done')

def savedata():
    print('Saving data...')
    with open('tokens.txt', 'a') as a:
        a.write(account.token)
        a.write('\n')
    with open('username_and_passwords.txt', 'a') as a:
        a.write('Account details: Username: ' + account.username + ' Email: ' + account.email + ' Password: ' + account.password + ' Token: ' + account.token)
        a.write('\n')
    if exit_when_done == True:
        driver.quit()
        #sys._exit()
    #if auto_join == True:
     #   print('Auto joining...')
      #  Auto_Join()

def token():
    print('Getting the token...')
    l_storage = LocalStorage(driver)
    token = l_storage.get("token")
    token = token[1:-1]
    account.token = token
    print('Account details: Usermame: ' + account.username + ' Email: ' + account.email + ' Password: ' + account.password  + ' Token: ' + account.token)
    savedata()

def claim_account():
    global x
    try:
        date_enter_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/div/div/div/form/div[4]/div/button')
    except:
        print('Error finding the button, retrying...')
        claim_account()
    if date_enter_button.is_enabled() == True:
        try:
       #     print()
            date_enter_button.click()
            print('Entered the date')
            claim_account1()
        except:
            print('Retrying')
            time.sleep(1)
            claim_account()
    else:
        print('Waiting for the page to load')
        time.sleep(20)
        print('Done waiting')
        actions.send_keys('m')
        #actions.perform()
        #time.sleep(5)
        actions.send_keys(Keys.RETURN)
        actions.send_keys('7')
        actions.send_keys(Keys.RETURN)
        actions.send_keys('19')
        actions.send_keys(Keys.RETURN)
        actions.perform()
        time.sleep(3)
        claim_account()
        #if x == 0:
         #   print('The button is not visible, enter a date.')
          #  print('Enter a random data lol')
           # x = 1
            #claim_account()
        #else:
         #   time.sleep(0.1)
          #  claim_account()
          #the_month = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/div/div/div/form/div[3]/div[1]/div[1]/div/div/div/div/div[2]/div')
          

def claim_account1():
    try:
        the_x = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/button')
        the_x.click()
        print('xing that (1)')
        claim_account2()
    except:
        print('Retrying (1)')
        time.sleep(1)
        claim_account1()

def claim_account2():
    #if its a invilid email, make it use a valid one via a fake email
    try:
        claim_email = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/form/div[1]/div/input')
        claim_email.send_keys(email)
        time.sleep(2)
        claim_password = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/form/div[2]/div/input')
        claim_password.send_keys(password)
        time.sleep(2)
        Claim_Account = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/form/button')
        Claim_Account.click()
        print('Claimed account')
        time.sleep(5)
        claim_account3()
    except:
        print('Retrying(2)')
        time.sleep(1)
        claim_account2()

def claim_account3():
    global trys
    try:
        if trys == '5':
            print('Error... Geting the token')
            token()
        else:
            trys = trys + 1
            print('xing that (3)')
            the_second_x = driver.find_element_by_xpath('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[1]/button')#('//*[@id="app-mount"]/div[6]/div[2]/div/div/div[2]/button')
            the_second_x.click()
            print('xed that (3)')
            token()
    except:
        print('Retrying (3)')
        time.sleep(1)
        claim_account3()

cap = 0
claim = 'false'

argument_list = argv[1:]
if len(argument_list) > 0 and argument_list[0] == "claim_account":
    claim = 'true'
    print("Will claim the account")

if len(argument_list) == 0:
    print('Will not claim the token')

if len(argument_list) > 0 and argument_list[0] == 'help':
    print('use py Auto_alt_maker claim_account to claim the account it gennerates otherwise it will no claim the account')
    exit(0)

account = DiscordAccount()
account.generate_random_credentials()
username = account.username
if use_saved_email == True:
    with open('email.txt', 'r') as a:
        email = a.read()
    print('Using email ' + email)
else:
    email = account.email
#Need to add a way to make this random/diffrent
password = 'Soccer0127'
print("Makeing alt: " + username + " Email: " + email +
      " Password: " + password)

driver.get('https://discord.com/')
time.sleep(5)

try:
    Open_discord_in_your_browser = driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/button')
    Open_discord_in_your_browser.click()
except:
    driver.quit()
    sys.exit()
time.sleep(5)
Enter_a_username = driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/input')
Enter_a_username.send_keys(username)
time.sleep(5)
Enter_a_username_confurm_button = driver.find_element_by_xpath('//*[@id="app-mount"]/div/div/div[1]/div[2]/div/div[2]/form/button')
Enter_a_username_confurm_button.click()
while driver.current_url == 'https://discord.com/':
    if cap == 0:
        print('You need to do the captia')
        time.sleep(1)
        cap = 1
    else:
        time.sleep(1)
if claim == 'true':
    print('Claiming the account')
    time.sleep(5)
    claim_account()
else:
    account.email = 'There is no account email, this is not a claimed account'
    account.password = 'There is no account password, this is not a claimed account'
    print('Done')
    token()
