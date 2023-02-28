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


if __name__ == "__main__":
    r = call_api("교대역 병원", 1, 100)
    r1 = call_api("교대역 병원", 101, 100)
    r2 = call_api("교대역 병원", 201, 100)
    r3 = call_api("교대역 병원", 301, 100)
    r4 = call_api("교대역 병원", 401, 100)
