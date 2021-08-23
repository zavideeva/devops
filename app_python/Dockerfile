FROM python:3.9-alpine3.14
WORKDIR /code

RUN adduser -D myuser && chown -R myuser /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

USER myuser

ENTRYPOINT [ "gunicorn", "-b 0.0.0.0:8000", "main:APP" ]