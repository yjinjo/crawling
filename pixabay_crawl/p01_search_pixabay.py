import chromedriver_autoinstaller
from selenium import webdriver
import ssl
import time

from urllib.request import Request, urlopen

from selenium.webdriver.common.by import By

ssl._create_default_https_context = ssl._create_unverified_context

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
driver.implicitly_wait(1)

url = "https://pixabay.com/ko/images/search/사과/"
driver.get(url=url)


image_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div[3]/div[1]/div/div/div/a/img"
image_url = driver.find_element(By.XPATH, image_xpath).get_attribute("src")
print(f"image_url: {image_url}")

image_byte = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
f = open("apple.jpg", "wb")
f.write(urlopen(image_byte).read())
f.close()

time.sleep(30)
