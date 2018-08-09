#!/usr/bin/env python
# -*- coding:utf-8 -*-

# -----<缩略图>----- #

import os, datetime
from PIL import Image


def ThumbNailImg(infile):
    # 略缩图路径
    outfile = os.path.splitext(infile)[0] + "_ThumbNail" + ".jpeg"
    im = Image.open(infile)
    height_img = int(im.size[1] * 750 / im.size[0])
    size = (206, 206)
    im.thumbnail(size, Image.ANTIALIAS)
    im.save(outfile)
    return outfile
