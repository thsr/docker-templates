FROM python:3.6-alpine

WORKDIR app

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY ./src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python", "./app.py" ]