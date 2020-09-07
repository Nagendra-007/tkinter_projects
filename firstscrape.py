from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

my_url="https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card"
uclient = urlopen(my_url)
page_html = uclient.read()
uclient.close()

page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("div", { "class" : "item-container" })
filename = "products.csv"
f = open(filename, "w")
headers = "product_name, product_brand, product_price, shipping_price\n"
f.write(headers)
for i in range(len(containers)):
    container = containers[i]
    c = container.find("div", {"class" : "item-info"})
    p = container.find("li", {"class" : "price-current"})
    s = container.find("li", {"class" : "price-ship"})
    n = container.find("a", {"class" : "item-title"})
    product_brand = c.div.a.img["title"]
    product_name = n.text
    product_price = p.strong.text
    shipping_price = s.text.strip()
    f.write(product_name.replace(",", "|") + "," + product_brand + "," + product_price + "," + shipping_price +"\n")
f.close()
