# -*- coding: utf-8 -*-
# @Author: bingyangl
# @Date:   2025-06-11 19:52:30
# @Last Modified by:   55037
# @Last Modified time: 2025-06-12 04:32:26
import requests
import base64

def getbs64(path):
    with open(path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

url = "http://192.168.31.30:9898/ocr"

url1 = "http://192.168.31.30:9898/slide_match"
image_path = "H5jW2j.png"
tg = getbs64("tg1.jpg")
bg =  getbs64("bg1.jpg")

# print(tg)
# print('\n')
# print(bg)
data = {
    "image": getbs64(image_path),
    "probability": False,
    "png_fix": False
}

data1 = {
"target": tg,
"background" : bg,
"simple_target": False
}
# print(data1)
response = requests.post(url, data=data)
print(response.json())


response = requests.post(url1, data=data1)
print(response.json())
res = response.json()['data']
print(f'滑动验证：向X轴正方向滑动{res['target'][0] - res['target_x']}像素')