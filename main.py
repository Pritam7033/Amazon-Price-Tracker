import requests
from bs4 import BeautifulSoup
import smtplib
my_email = "Type your mail here"
password = "Type you email password"
reciever_email = "type reciever mail address."
URL = "https://www.amazon.in/Airdopes-141-Bluetooth-Wireless-Playtime/dp/B09N3ZLB3T?th=1"

headers = {
    "User-Agent":"Your user agent details",
    "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
}

response = requests.get(url=URL, headers=headers)
html_data = response.text

soup = BeautifulSoup(html_data, "html.parser")
amount = soup.find(name="span", class_="a-price-whole")
price_text = amount.get_text()
if "," in price_text:
    price_text = price_text.replace(",", "")
price = int(price_text.replace(".", "").strip())
print(price)
if price <= 1100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=reciever_email,
            msg=f"subject:Price-Drop\n\nThe Airpods-141 price dropped current Price is {price}. you can now purchase it."
        )
