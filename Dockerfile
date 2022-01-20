FROM python:3.8.12-buster

WORKDIR /travel

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ['python','run.py']

