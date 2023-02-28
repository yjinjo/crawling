from typing import Dict

import pandas as pd
import requests
from bs4 import BeautifulSoup


def crawl(code: str) -> Dict[str, str]:
    # Crawling
    url = f"https://finance.naver.com/item/main.nhn?code={code}"
    res = requests.get(url)

    # Parsing
    bs_obj = BeautifulSoup(res.text, "html.parser")

    div_today = bs_obj.find("div", {"class": "today"})
    price = div_today.find("span", {"class": "blind"}).text

    wrap_company = bs_obj.find("div", {"class": "wrap_company"})
    name = wrap_company.a.text

    div_description = wrap_company.find("div", {"class": "description"})
    code = div_description.span.text

    table_no_info = bs_obj.find("table", {"class": "no_info"})
    tds = table_no_info.tr.find_all("td")
    volume = tds[2].find("span", {"class": "blind"}).text

    dic = {"name": name, "price": price, "code": code, "volume": volume}
    return dic


codes = ["035720", "005930", "051910", "000660"]

company_lst = list()
for code in codes:
    company_lst.append(crawl(code))

df = pd.DataFrame(company_lst)
print(df)
