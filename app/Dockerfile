FROM python:3.10
EXPOSE 5000
WORKDIR /app

# change directory
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "--app", "app", "run", "--debug", "--host", "0.0.0.0"]