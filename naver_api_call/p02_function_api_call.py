import requests

from dotenv import load_dotenv
import os

load_dotenv()


def call_api(keyword, start, display):
    url = f"https://openapi.naver.com/v1/search/blog.json?query={keyword}&start={start}&display={display}"
    res = requests.get(
        url,
        headers={
            "X-Naver-Client-Id": os.environ.get("X_NAVER_CLIENT_ID"),
            "X-Naver-Client-Secret": os.environ.get("X_NAVER_CLIENT_SECRET"),
        },
    )
    r = res.json()
    print(len(r["items"]))
    return r


def get_paging_call(keyword, quantity):
    repeat = 9

    for i in range(repeat):
        print(f"{i + 1}번 반복 합니다.")


if __name__ == "__main__":
    # r = call_api("교대역 병원", 1, 100)
    r = get_paging_call("교대역 이비인후과", 900)
