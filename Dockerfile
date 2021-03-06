FROM python:alpine3.6

WORKDIR /opt/insta/

COPY requirements.txt ./

RUN apk --update add python3 tzdata

ENV TZ=Asia/Bishkek

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip3 install --no-cache-dir gunicorn

RUN rm -rf /var/cache/apk/*

COPY . .

EXPOSE 5000

ENV FILE_PATH=/opt/insta/gif1.zip

ENV INSTAGRAM_USERNAME=name
ENV INSTAGRAM_PASSWORD=pass

CMD gunicorn --bind 0.0.0.0:5000 app:app
