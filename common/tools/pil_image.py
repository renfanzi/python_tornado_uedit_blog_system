#!/usr/bin/env python
# -*- coding:utf-8 -*-

# -----<缩略图>----- #

import os, datetime
from PIL import Image


def ThumbNailImg(infile):
    # 略缩图路径
    img = Image.open(infile)
    width, height = img.size
    # 裁剪图片成正方形
    if width > height:
        delta = (width - height) / 2
        box = (delta, 0, width - delta, height)
        region = img.crop(box)
    elif height > width:
        delta = (height - width) / 2
        box = (0, delta, width, height - delta)
        region = img.crop(box)
    else:
        region = img

        # 缩放
    thumb = region.resize((535, 256), Image.ANTIALIAS)
    filename = os.path.splitext(infile)[0] + "_ThumbNail" + ".gif"
    # 保存
    thumb.save(filename, quality=70)
    return filename
