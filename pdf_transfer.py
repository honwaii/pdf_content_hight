#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 0017 11:26
# @Author  : honwaii
# @Email   : honwaii@126.com
# @File    : controller.py

import os


def pdf_to_html(file_name):
    os.system(
        'copy E:\\projects\\2020\\pdf_content_hight\\app\\datas\\' + file_name + ' D:\\pdf2htmlEX\\works\\' + file_name)
    os.chdir('D:\\pdf2htmlEX')
    os.system(
        'pdf2htmlEX.exe --zoom 1.8 --dest-dir E:\\projects\\2020\\pdf_content_hight\\app\\datas ./works/' + file_name)
    return


pdf_to_html('test.pdf')
