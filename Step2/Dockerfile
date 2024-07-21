FROM python:3.9-slim
MAINTAINER Igor Nikolayenko
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "rick_and_morty.py"]
