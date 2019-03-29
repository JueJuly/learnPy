# -*- coding: UTF8 -*-
import time
import datetime
import os
from PIL import Image

im = Image.open("./img_pyplot.jpg")
new_im = im.convert('P')
print(new_im.mode)
new_im.show()
