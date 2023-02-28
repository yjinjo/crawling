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
import multiprocessing

load_dotenv()

ssl._create_default_https_context = ssl._create_unverified_context

# 크롬드라이버 install
chromedriver_autoinstaller.install()

driver = webdriver.Chrome()

# 인스타 같은 경우는 로딩이 그렇게 빠르지 않기 때문에 3초 정도 기다렸다가 불러오는 것으로 설정
driver.implicitly_wait(5)

url = "https://www.instagram.com/"
driver.get(url=url)


def login(instagram_id: str, instagram_pw: str):
    id_x_path = "//*[@id='loginForm']/div/div[1]/div/label/input"
    input_id = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, id_x_path)))
    input_id.send_keys(instagram_id)

    pw_x_path = "//*[@id='loginForm']/div/div[2]/div/label/input"
    input_pw = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, pw_x_path)))
    input_pw.send_keys(instagram_pw)

    login_x_path = "//*[@id='loginForm']/div/div[3]/button"

    login = driver.find_element(By.XPATH, login_x_path)
    # login = wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, login_x_path)))
    # login.click()
    login.send_keys(Keys.ENTER)

    time.sleep(5)


def search(hashtag: str, scroll_times: int):
    url = f"https://www.instagram.com/explore/tags/{hashtag}/"
    driver.get(url=url)

    time.sleep(3)

    for _ in range(scroll_times):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)


def like_comment(nth, comment, repeat=3):
    row = (nth - 1) // 3 + 1
    col = (nth - 1) % 3 + 1
    # nth Post 클릭
    xpath = f"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/article/div[2]/div/div[{row}]/div[{col}]"
    driver.find_element(By.XPATH, xpath).click()

    for _ in range(repeat):
        # like
        like_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button"
        driver.find_element(By.XPATH, like_xpath).click()

        # comment
        comment_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/textarea"
        driver.find_element(By.XPATH, comment_xpath).click()
        driver.find_element(By.XPATH, comment_xpath).send_keys(comment)

        # 게시 버튼 누르기
        comment_button_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/article/div/div[2]/div/div/div[2]/section[3]/div/form/div/div[2]"
        driver.find_element(By.XPATH, comment_button_xpath).click()

        # 다음 게시물 선택
        next_button_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[3]/div/div/div/div/div[1]/div/div/div[2]/button"
        driver.find_element(By.XPATH, next_button_xpath).click()


if __name__ == "__main__":
    processes = []

    # Login
    instagram_id = os.environ.get("INSTAGRAM_ID")
    instagram_pw = os.environ.get("INSTAGRAM_PW")
    login(instagram_id, instagram_pw)

    # Search
    hashtag = "강아지"
    search(hashtag=hashtag, scroll_times=0)

    # Like Comment
    like_comment(4, "강아지가 귀엽네요", 2)

    time.sleep(100)
