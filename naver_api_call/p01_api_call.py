import requests

from dotenv import load_dotenv
import os

load_dotenv()

url = "https://openapi.naver.com/v1/search/blog.json?query=강남역 맛집&start=1&display=100"
res = requests.get(
    url,
    headers={
        "X-Naver-Client-Id": os.environ.get("X_NAVER_CLIENT_ID"),
        "X-Naver-Client-Secret": os.environ.get("X_NAVER_CLIENT_SECRET"),
    },
)
r = res.json()

print(len(r["items"]))

for item in r["items"]:
    print(item)
