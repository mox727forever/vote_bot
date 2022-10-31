FROM python:3.10.4-alpine

WORKDIR /usr/src/app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt
ENV CONFIG_NAME="config.ini"
CMD ["python", "main.py"]
