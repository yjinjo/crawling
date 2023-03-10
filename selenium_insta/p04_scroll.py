from selenium import webdriver
import chromedriver_autoinstaller
import ssl
import time
import os
from dotenv import load_dotenv
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait

load_dotenv()

ssl._create_default_https_context = ssl._create_unverified_context

# 크롬드라이버 install
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 인스타 같은 경우는 로딩이 그렇게 빠르지 않기 때문에 3초 정도 기다렸다가 불러오는 것으로 설정
driver.implicitly_wait(3)

url = "https://www.instagram.com/"
driver.get(url=url)

id_x_path = "//*[@id='loginForm']/div/div[1]/div/label/input"
instagram_id = os.environ.get("INSTAGRAM_ID")

# input_id = driver.find_element(By.XPATH, x_path)
input_id = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, id_x_path)))
input_id.send_keys(instagram_id)

pw_x_path = "//*[@id='loginForm']/div/div[2]/div/label/input"
instagram_pw = os.environ.get("INSTAGRAM_PW")

input_pw = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pw_x_path)))
input_pw.send_keys(instagram_pw)

login_x_path = "//*[@id='loginForm']/div/div[3]/button"

login = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_x_path)))
# login.click()
login.send_keys(Keys.ENTER)

time.sleep(3)

# Search
hashtag = "강아지"
url = f"https://www.instagram.com/explore/tags/{hashtag}/"
driver.get(url=url)

for _ in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)


time.sleep(100)
