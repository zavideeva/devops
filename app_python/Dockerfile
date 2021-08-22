FROM python:3.8
WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENTRYPOINT [ "gunicorn", "-b 0.0.0.0:8000", "main:APP" ]