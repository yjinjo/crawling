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

time.sleep(3)

image_area_xpath = "/html/body/div[1]/div[2]/div/div[3]/div/div[3]"
image_area = driver.find_element(By.XPATH, image_area_xpath)
image_elements = image_area.find_elements(By.TAG_NAME, "img")

image_urls = list()
for image_elemnt in image_elements:
    if image_elemnt.get_attribute("data-lazy") is None:
        image_urls.append(image_elemnt.get_attribute("src"))
    else:
        image_urls.append(image_elemnt.get_attribute("data-lazy"))

for i in range(len(image_urls)):
    image_url = image_urls[i]
    image_byte = Request(image_url, headers={"User-Agent": "Mozilla/5.0"})
    f = open(f"apple{i}.jpg", "wb")
    f.write(urlopen(image_byte).read())
    f.close()
