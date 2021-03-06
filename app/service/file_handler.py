#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 0024 15:21
# @Author  : honwaii
# @Email   : honwaii@126.com
# @File    : file_handler.py

import os
import re
from functools import reduce

import gensim as gensim

from app.util.cfg_operator import config
import jieba
import pandas as pd


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


def extract_text():
    os.system('pdf2txt.py -o ".\\datas\\temp.txt" -t text ".\\datas\\temp.pdf"')
    print("转换成文本完成")
    return


def handle_content():
    with open('.\\datas\\temp.txt', encoding='utf-8') as file:
        docs = file.readlines()
        doc = reduce(lambda x, y: x + y, docs)
    doc = doc.replace("\r", "").replace("\n", "")
    re_words = re.compile(u".*?([\u4E00-\u9FA5]+).*?")
    doc_str = re.findall(re_words, doc)
    content = reduce(lambda x, y: x + y, doc_str)
    word_list = jieba.lcut(content)
    with open('./datas/中文停用词表.txt', encoding='utf-8') as reader:
        stop_words = reader.read().split("\n")
    result = []
    for each in word_list:
        if each in stop_words:
            continue
        result.append(each)
    return result


def load_word_embedding_model():
    path = config.get_config('')
    word_embedding = gensim.models.Word2Vec.load(path)
    return word_embedding
