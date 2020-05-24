#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 0024 15:21
# @Author  : honwaii
# @Email   : honwaii@126.com
# @File    : file_handler.py

import os
import  pdfminer

def pdf_convert(file=None):
    current_path = os.getcwd()
    print(current_path)
    os.system('COPY ".\\datas\\temp.pdf" "D:\\pdf2htmlEX\\works\\"')
    os.chdir("D:/pdf2htmlEX")
    # print(os.getcwd())
    os.system('pdf2htmlEX.exe --zoom 1.8  --dest-dir ".\\works" ".\\works\\temp.pdf"')
    if os.path.exists('.\\works\\temp.html'):
        os.system('move ".\\works\\temp.html" "' + current_path + '\\datas\\temp.html"')
        os.chdir(current_path)
    return
