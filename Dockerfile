FROM daocloud.io/library/python:3.6
ENV PYTHONUNBUFFERED 1
RUN sed -i 's/deb.debian.org/mirrors.ustc.edu.cn/g' /etc/apt/sources.list
RUN mkdir /code
WORKDIR /code
ADD requirments.txt /code
RUN pip install -r requirments.txt -i https://pypi.mirrors.ustc.edu.cn/simple
