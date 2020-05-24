#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 0017 11:26
# @Author  : honwaii
# @Email   : honwaii@126.com
# @File    : controller.py
import os

from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import secure_filename, redirect
from app.service import file_handler

app = Flask(__name__)
# bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route("/", methods=['POST', 'GET'])
def index():
    return render_template('index.html')


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method != 'POST':
        return ""
    file = request.files['file']
    if file is None:
        return "未选择文件，上传的文件为空"
    file_name = str(secure_filename(file.filename)).strip()
    print(str(file_name))
    if file_name.endswith('.pdf') is not True:
        return '上传的不是pdf文件。'
    file.save('./datas/temp.pdf')
    file_handler.pdf_convert()
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
