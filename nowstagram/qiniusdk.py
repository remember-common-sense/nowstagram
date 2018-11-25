# -*- coding: utf-8 -*-

from nowstagram import app
from qiniu import Auth, put_stream, put_data
import os

#需要填写你的 Access Key 和 Secret Key
access_key = app.config['QINIU_ACSESS_KEY']
secret_key = app.config['QINIU_SECRET_KEY']

q = Auth(access_key, secret_key)

#要上传的空间
bucket_name = app.config['QINIU_BUCKET_NAME']

def qiniu_upload_file(source_file, save_file_name):
    # 生成上传Token，可以指定过期时间等
    token = q.upload_token(bucket_name, save_file_name)

    ret, info = put_data(token, save_file_name, source_file.stream)

    print(info)







