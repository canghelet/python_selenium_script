from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://carturesti.ro/')
driver.maximize_window()

# get all the links of the webpage
links = driver.find_elements(By.XPATH, '//a[@href]')
for link in links:
    print(link.get_attribute("innerHTML"))

# locate search bar and perform action by entering carti text and return the results
searchBar = driver.find_element(By.ID, "search-input")
searchBar.clear()
searchBar.send_keys("carti")
searchBar.send_keys(Keys.RETURN)
time.sleep(3)

# locate book elements and add them to cart
driver.find_element(By.XPATH, '//*[@id="coloana-produse"]/div/div/div[1]/prod-grid-box/a/div/img').click()
driver.find_element(By.XPATH, '//*[@id="cartu-add-to-cart-btn-x"]/a').click()
driver.back()
time.sleep(3)

driver.find_element(By.XPATH, '//*[@id="coloana-produse"]/div/div/div[6]/prod-grid-box/a/div/img').click()
driver.find_element(By.XPATH, '//*[@id="cartu-add-to-cart-btn-x"]/a').click()
driver.back()
time.sleep(3)

# return the length of list with all elements having a specific class name
driver.get('https://carturesti.ro/')
items = driver.find_elements(By.CLASS_NAME, "ng-scope")
print(len(items))
time.sleep(3)

# open https://carturesti.ro/info/despre-carturesti-ro page
driver.find_element(By.ID, "carturestiDropdown").click()
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[1]/ul/li[1]/a').click()
time.sleep(3)

# open https://carturesti.ro/librarii page
driver.find_element(By.ID, "carturestiDropdown").click()
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[1]/ul/li[2]/a').click()
time.sleep(3)

# open https://carturesti.ro/blog page
driver.find_element(By.ID, "carturestiDropdown").click()
driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div/div[2]/md-menu-bar[2]/md-menu-item[1]/ul/li[3]/a').click()
time.sleep(3)
driver.back()

# fill in web form and subscribe to newsletter
driver.get('https://carturesti.ro/')
email = driver.find_element(By.XPATH, '//*[@id="mce-EMAIL"]')
email.send_keys("angheletcristina@yahoo.com")
time.sleep(3)

last_name = driver.find_element(By.XPATH,  '//*[@id="mce-FNAME"]')
last_name.send_keys("Anghelet")
time.sleep(3)

first_name = driver.find_element(By.XPATH, '//*[@id="mce-LNAME"]')
first_name.send_keys("Cristina")
time.sleep(3)

subscribe_newsletter = driver.find_element(By.XPATH, '//*[@id="mc-embedded-subscribe"]')
time.sleep(3)
subscribe_newsletter.click()
time.sleep(3)
driver.close()
