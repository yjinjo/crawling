from selenium import webdriver
import chromedriver_autoinstaller
import ssl
import time

ssl._create_default_https_context = ssl._create_unverified_context

# 크롬드라이버 install
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 인스타 같은 경우는 로딩이 그렇게 빠르지 않기 때문에 3초 정도 기다렸다가 불러오는 것으로 설정
driver.implicitly_wait(3)

url = "https://www.instagram.com/"
driver.get(url=url)
time.sleep(20)
