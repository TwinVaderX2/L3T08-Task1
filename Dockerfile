FROM python:3.8-slim-buster

WORKDIR /app

COPY src/* ./

CMD [ "./inventory.py"]
ENTRYPOINT [ "python3" ]