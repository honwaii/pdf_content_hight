#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/17 0017 11:26
# @Author  : honwaii
# @Email   : honwaii@126.com
# @File    : controller.py
import os

from flask import Flask, render_template, request, flash, url_for
from werkzeug.utils import secure_filename, redirect

app = Flask(__name__)
# bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = os.urandom(24)


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        f = request.files.get('fileupload')
        basepath = os.path.dirname(__file__)
        if f:
            filename = secure_filename(f.filename)
            types = ['jpg', 'png', 'tif']
            if filename.split('.')[-1] in types:
                uploadpath = os.path.join(basepath, 'static/uploads', filename)
                f.save(uploadpath)
                flash('Upload Load Successful!', 'success')
            else:
                flash('Unknown Types!', 'danger')
        else:
            flash('No File Selected.', 'danger')
        return redirect(url_for('index'))
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
