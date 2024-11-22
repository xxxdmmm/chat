# 使用官方的 Python 镜像作为基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 拷贝项目的代码到容器中
COPY ./chat /app/

WORKDIR /app/chat

# 安装系统依赖和 Python 依赖
RUN apt-get update && apt-get install -y \
    libmysqlclient-dev && \
    pip install --no-cache-dir -r requirements.txt

