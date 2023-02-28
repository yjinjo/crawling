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
    if quantity > 1100:
        exit("Error! 최대 요청할 수 있는 건수는 1100건 입니다.")
    repeat = quantity // 100
    result = list()
    for i in range(repeat):
        start = i * 100 + 1
        if start > 1000:
            start = 1000
        print(f"{i + 1}번 반복 합니다. start: {start}")
        r = call_api(keyword, start=start, display=100)
        result += r["items"]
    return result


if __name__ == "__main__":
    r = get_paging_call("강남역 파스타", 1100)
    print(len(r))
