# !/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/24 0024 15:38
# @Author  : honwaii
# @Email   : honwaii@126.com
# @File    : html_generate.py
import re
from functools import reduce

import gensim
import jieba
import jieba.analyse
from bs4 import BeautifulSoup
from gensim.models import KeyedVectors

from app.util.cfg_operator import config


def handle_content():
    load_word_embedding_model()

    with open('./datas/temp.txt', encoding='utf-8') as file:
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


def load_word_embedding_model(path=None):
    path = config.get_config('word_embedding_path')
    # word_embedding = gensim.models.Word2Vec.load(path)
    word_vector_model = KeyedVectors.load_word2vec_format(path)
    return word_vector_model


def result_words():
    key_words = handle_content()
    result = []
    for each in key_words:
        try:
            similar = word_embedding.most_similar(positive=each[0], topn=5)
            result.append(similar)
        except KeyError:
            continue
    words = []
    for each in result:
        for e in each:
            words.append(e[0])
    return words


def parse_html_and_add_style():
    soup = BeautifulSoup(open('./datas/temp.html', encoding='utf-8'), features='html.parser')
    head = soup.head
    body = soup.body
    style = soup.new_tag('style')
    style.string = 'mark{background-color:#ffff00; font-weight:bold;}'
    head.append(style)
    head = str(head).replace("{#", "{ #")
    body = str(body).replace("{#", "{ #")
    return head, body


def highlight_word(word, doc):
    highlight = "<mark>" + word + "</mark>"
    doc = doc.replace(word, highlight)
    return doc


def get_highlight_content():
    words = result_words()
    head, body = parse_html_and_add_style()
    temp = '<!DOCTYPE html> \n \
    <html xmlns="http://www.w3.org/1999/xhtml">'
    for word in words:
        body = highlight_word(word, body)
    with open('./templates/result.html', 'w', encoding='utf-8') as f:
        f.write(temp)
        f.write(head)
        f.writelines(body)
        f.write('</html>')
        f.flush()
        f.close()
    return


word_embedding = load_word_embedding_model()
