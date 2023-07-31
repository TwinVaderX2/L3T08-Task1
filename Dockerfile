FROM python:3.8-slim-buster

WORKDIR /app

COPY . .

CMD [ "./src/app/inventory.py"]
ENTRYPOINT [ "python3" ]