#!/bin/bash

# 执行数据库迁移
python3 manage.py makemigrations

python3 manage.py migrate

python3 manage.py collectstatic --noinput

# 启动 Django 开发服务器
python3 manage.py runserver 0.0.0.0:8000
