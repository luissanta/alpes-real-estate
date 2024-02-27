FROM python:3.10-alpine

WORKDIR /alpes-real-estate

COPY . .

COPY config-cloud.py config.py

RUN pip install --no-cache-dir --upgrade -r requirements.txt

EXPOSE 80

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]