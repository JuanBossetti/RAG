# docker run --env-file .env -v /mnt/datos/desarrollo/huggingface-models:/app/models -v /mnt/datos/desarrollo/documentos:/app/docs -e PORT=7000 -p 8002:7000 --network ninguna adobe

FROM python:3.9-slim-buster

RUN pip install --upgrade pip==20.0.2

RUN mkdir -p /app/models
RUN mkdir -p /app/docs

VOLUME /app/models
VOLUME /app/docs

WORKDIR /app

ENV HF_HOME=/app/models/
ENV BASE_PATH=/app/docs
ENV PATH_PDF=/app/docs/pdf

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader punkt

# Comando para verificar si la variable de entorno PORT está definida y ejecutar la aplicación
CMD ["sh", "-c", "if [ -z \"$PORT\" ]; then echo 'Error: PORT variable is not set'; exit 1; fi; export FLASK_APP=api_adobe.py && flask run --host=0.0.0.0 --port=${PORT}"]
