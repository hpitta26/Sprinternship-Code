FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY app.py .

# Use Mongo container hostname; requires API + mongo on the same Docker network (see commands).
ENV MONGODB_URL=mongodb://mongodb:27017

EXPOSE 80

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]