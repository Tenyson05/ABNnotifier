from time import sleep
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.bestbuy.com/site/evga-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card/6436191.p?skuId=6436191&intl=nosplash")

#define loop to refresh page 3 times
while True:
	sleep(70)
	print("refreshing...")
	driver.refresh()

