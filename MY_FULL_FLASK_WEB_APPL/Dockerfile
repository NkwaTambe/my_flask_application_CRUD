FROM python:3.11

ENV FLASK_ENV=production

# App, specify permission to this
WORKDIR /MY_FULL_FLASK_WEB_APPL

COPY . .

RUN pip install -r requirements.txt

EXPOSE 8000

CMD flask run --host=0.0.0.0