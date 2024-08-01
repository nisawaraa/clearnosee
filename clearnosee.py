import requests
from bs4 import BeautifulSoup
import csv
# ดึงข้อมูลจากเว็บไซต์ 
page = requests.get('https://www.konvy.com/brand/clear-nose-1/?searchTit=CLEAR+NOSE')
soup = BeautifulSoup(page.content, 'html.parser')

# ดึงชื่อสินค้า
product = soup.find_all('p', class_='product-name')
product_names = [p.get_text().strip() for p in product]

# ดึงส่วนลด
discounts = soup.find_all('span', class_='product-Discount')
product_Discounts = [d.get_text().strip() for d in discounts]

# ดึงรีวิว
reviews = soup.find_all('p', class_='product-Reviews')
product_Reviews = [r.get_text().strip() for r in reviews]

# ดึงราคาปัจจุบัน
Price= soup.find_all('p', class_='product-Price')
product_Price= [r.get_text().strip() for r in Price]

# ดึงราคาก่อนหน้า
Del= soup.find_all('del', class_='product-del')
product_del =[r.get_text().strip() for r in Del]


# แสดงผลที่เราดึงมา
print("ชื่อสินค้า:", product_names)
print("ส่วนลด:", product_Discounts)
print("รีวิว:", product_Reviews)
print("ราคา:", product_Price)
print("ราคา:",product_del)


with open('clearnosee.csv', 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Product_names', 'Discount', 'Reviews_rate', 'Price'])
    for product, discounts, reviews, price in zip(product_names, product_Discounts, product_Reviews, product_Price):
        writer.writerow([product, discounts, reviews, price])
    print("Data .csv file saved")