# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 0024 15:38
# @Author  : honwaii
# @Email   : honwaii@126.com
# @File    : test.py
import os
import re
from functools import reduce

import gensim
import jieba
import jieba.analyse
from app.util.cfg_operator import config


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

    sentence = reduce(lambda x, y: x + y, result)
    keywords = jieba.analyse.extract_tags(sentence, topK=20, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    print(keywords)
    return keywords


def load_word_embedding_model():
    path = config.get_config('word_embedding_path')
    word_embedding = gensim.models.Word2Vec.load(path)
    return word_embedding


def result_words():
    word_embedding = load_word_embedding_model()
    key_words = handle_content()
    result = []
    for each in key_words:
        t = word_embedding.most_similar(positive=each[0], topn=5)
        result.append(t)
        print(t)


result_words()
