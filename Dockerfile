FROM python
RUN pip3 install pymysql
RUN pip3 install redis
RUN mkdir /src
COPY . /src