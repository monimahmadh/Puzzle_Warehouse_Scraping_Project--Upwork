import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.puzzlewarehouse.com/jigsaw-puzzles-piece-count-100/?aid=&pcs=&cid=&sort=productNameAsc&usa=0&show=472&stock=1&store=0&budget_from=0&budget_to=0&price=0"

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "lxml")

products_divs = soup.find_all("div", class_="col-6 col-sm-6 col-lg-4 product-list-item")
# print(items_div[0:4])

master_list = []


def product_details(product):
    product_name = product.find("div", class_="product-link").text

    product_price = product.find("div", class_="product-price").find("span").text

    product_url_div = product.find("div", class_="col-12 align-items-center")
    product_url = str(product_url_div.find("a")).split("\"")[1]

    all_of_one_item = {"Product Name": product_name, "Price": product_price, "Url": product_url}

    master_list.append(all_of_one_item)


for product in products_divs:
    product_details(product)

data_frame = pd.DataFrame(master_list)
data_frame.to_csv("test5.csv", index=False)

print("Done")
