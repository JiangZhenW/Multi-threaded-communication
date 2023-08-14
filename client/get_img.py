import requests
import re
from bs4 import BeautifulSoup
import queue
from utils.constants import *
import os

"""
Author: Zhenwei Jiang
Finished Time: 13-8-2023
Function: Crawl images and save these images.
"""


def get_img(target, url, img_queue: queue.Queue):
    path = DATA_PATH
    if not os.path.exists(path):
        os.makedirs(path)
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    soup = BeautifulSoup(resp.text, 'html.parser')
    addresses = re.findall('src="https:.*?"', str(soup))
    for idx in range(len(addresses)):
        address = addresses[idx].replace("src=", "")[1:-1]
        # print(address)
        pic = requests.get(address+'.jpg').content
        with open(path+f'/{target}_{idx}.jpg', 'wb') as f:
            f.write(pic)
            img_queue.put(path+f'/{target}_{idx}.jpg')

