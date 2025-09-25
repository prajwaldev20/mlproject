FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt /app/
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc g++ ffmpeg libsm6 libxext6 unzip \
 && pip install --no-cache-dir --upgrade pip setuptools wheel \
 && pip install --no-cache-dir -r requirements.txt \
 && apt-get purge -y build-essential gcc g++ \
 && apt-get autoremove -y \
 && rm -rf /var/lib/apt/lists/*
COPY . /app
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "application:application"]