FROM python

WORKDIR /app

COPY . .

RUN pip install flask
RUN pip install pymysql
RUN apt update
RUN apt install nano
RUN pip install cryptography

CMD ["python", "app.py"]