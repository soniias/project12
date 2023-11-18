import requests
from bs4 import BeautifulSoup
import lxml

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