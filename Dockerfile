FROM python:3.9-slim
WORKDIR /my-app
COPY requirements.txt .
RUN pip-install -r requirements.txt
COPY . .
CMD ["Python", "app.py"]