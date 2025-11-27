FROM python:3.13-slim

WORKDIR .

COPY . .

RUN pip install --no-cache-dir -r requirements.txt | true

COPY . .

CMD ["python3", "main.py"]



