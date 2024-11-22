#!/bin/bash

# 执行数据库迁移
python manage.py makemigrations

python manage.py migrate

# 启动 Django 开发服务器
python manage.py runserver 0.0.0.0:8000
