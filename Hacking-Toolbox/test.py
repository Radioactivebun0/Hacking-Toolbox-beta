from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

PROXY = "88.198.43.234:3128" # IP:PORT or HOST:PORT

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--proxy-server=%s' % PROXY)

chrome = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
chrome.get("https://www.google.com/search?q=what+is+my+ip&rlz=1C1ONGR_enUS928US928&oq=what+is+my+ip&aqs=chrome..69i57.2590j0j4&sourceid=chrome&ie=UTF-8")