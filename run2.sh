#!/bin/bash

python3 manage.py collectstatic --noinput

# 启动 Django 开发服务器
python3 manage.py runserver 0.0.0.0:8000
