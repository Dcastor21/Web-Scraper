from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO

search =  input ("search for:")
params = {"q": search}
r = requests.get("http://www.bing.com/images/search", params=params)
soup = BeautifulSoup(r.text,"html.parser")
links = soup.findAll("a", {"cass":"thumb"})

for item in links:
    img_obj = requests.geet(item.attrs["href"])
    print("retreving:",item.attrs["herf"])
    title = item.attrs["href"].split["/"][-1]
    img = Image.open(BytesIO(img_obj.content))
    img.save("./scraped_img/"+title, img.format)
