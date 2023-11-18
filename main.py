# import requests
# from bs4 import BeautifulSoup
# import lxml
# import openpyxl
#
#
# user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#         "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
# headers = {"User-agent": user}
# session = requests.Session()
# book = openpyxl.Workbook()
# book.save("catalog.xlsx")
# sheet = book.active
# sheet["A1"] = "Title company"
# sheet["B1"] = "Percent"
# for j in range(1, 7):
#         print(f"Page {j}")
#                 url = f"https://cash-backer.club/shops?page={j}"
#                 response = session.get(url, headers=headers)
#                 if response.status_code == 200:
#                         soup = BeautifulSoup(response.text, "lxml")
#                         all_products = soup.find_all('div', class_="col-lg-2 col-md-3 "
#                                                                    "shop-list-card pseudo-link no-link")
#                         for i in all_products:
#                                 title = i.find('div', class_="shop-title")
#                                 cashback = i.find("div", class_="shop-rate")
#                                 print(title.text, cashback.text)
#                                 file.write(f"{title.text} {cashback.text} \n")
#                         for i in range(count, len(all_products)+count):
#                                 title = all_products[i].find('div', class_="shop-title")
#                                 cashback = all_products[i].find("div", class_="shop-rate")
#                                 sheet[f"A{i}"] = title.text
#                                 sheet[f"B{i}"] = cashback.text
#                                 count = len(all_products)
#
#
# book.save("catalog.xlsx")
# book.close()


# import requests
# from bs4 import BeautifulSoup
# import lxml
#
# url = "https://rozetka.com.ua/tablets/c130309/"
# user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#         "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
# headers = {"User-agent": user}
# session = requests.Session()
#
# for j in range(1, 68):
#     print(f"Page{j}")
#     url = f"https://rozetka.com.ua/tablets/c130309/page={j}/"
#     response = session.get(url, headers=headers)
#     # print(response.status_code)
#
#     if response.status_code == 200:
#             soup = BeautifulSoup(response.text, "lxml")
#             all_products = soup.find_all("li", class_="catalog-grid__cell catalog-grid__cell_type_slim ng-star-inserted")
#             for i in all_products:
#                 try:
#                     if i.find('div', class_="goods-tile__price--old price--gray ng-star-inserted"):
#                         price = i.find('span', class_="goods-tile__price-value")
#                         print(price.text)
#                         title = i.find('span', class_="goods-tile__title")
#                         print(title.text)
#                 except ValueError:
#                     print('Знижки немає')

import requests
from bs4 import BeautifulSoup
import lxml
import openpyxl

user = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36")
headers = {"User-agent": user}
session = requests.Session()

for j in range(1, 25):
    print(f"Page {j}")
    url = f"https://allo.ua/ua/televizory/p-{j}"
    response = session.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        all_products = soup.find_all('div', class_="product-card")
        for i in all_products:
            review = i.find('span', class_="review-button__text review-button__text--count")
            if i.find('div', class_="v-pb__cur discount"):
                with open("discount.txt", "a", encoding="utf-8") as file:
                    title = i.find('a', class_="product-card__title")
                    price = i.find('div', class_="v-pb__cur discount")
                    review = i.find('a', class_="review-button__link")
                    print(title.text, price.text, review.text)
                    file.write(f" Page {j} {title.text} {price.text} {review.text} reviews\n")
            elif i.find('div', class_="v-pb__cur"):
                with open("without_discount.txt", "a", encoding="utf-8") as file:
                    title = i.find('a', class_="product-card__title")
                    price = i.find('div', class_="v-pb__cur")
                    review = i.find('a', class_="review-button__link")
                    print(title.text, price.text, review.text)
                    file.write(f" Page {j} {title.text} {price.text} {review.text}reviews\n")