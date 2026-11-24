FROM python:2.7.18-slim
RUN pip install --no-cache-dir uncompyle6==3.9.2 xdis==6.1.1 spark-parser==1.8.9 click==7.1.2 six==1.16.0
