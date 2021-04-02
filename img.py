from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os
def ImgSearch():
    search =  input ("search for:")
    params = {"q": search}
    dir_name = search.replace(" ","_").lower
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)
    soup = BeautifulSoup(r.text,"html.parser")
    links = soup.findAll("a", {"cass":"thumb"})

    for item in links:
        try:
            img_obj = requests.geet(item.attrs["href"])
            print("retreving:",item.attrs["herf"])
            title = item.attrs["href"].split["/"][-1]
            try:
                img = Image.open(BytesIO(img_obj.content))
                img.save("./"+dir_name+"/"+title, img.format)
            except:
                print("could not Save image ")
        except:
            print("Could not collect Image")
     ImgSearch()
ImgSearch()