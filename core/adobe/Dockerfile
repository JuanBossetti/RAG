# docker run --env-file .env -v /mnt/datos/desarrollo/huggingface-models:/app/models -v /mnt/datos/desarrollo/documentos:/app/docs -e PORT=7000 -p 8002:7000 --network ninguna adobe

FROM python:3.9-slim-buster

RUN pip install --upgrade pip==24.3

RUN mkdir -p /app/models
RUN mkdir -p /app/docs/all_files/pdfs

VOLUME /app/docs

WORKDIR /app

ENV HF_HOME=/app/models/
ENV BASE_PATH=/app/docs
ENV USER_PATH=/all_files

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m nltk.downloader punkt

# Comando para verificar si la variable de entorno PORT está definida y ejecutar la aplicación con Gunicorn
CMD ["sh", "-c", "if [ -z \"$PORT\" ]; then echo 'Error: PORT variable is not set'; exit 1; fi; export FLASK_APP=api_adobe.py && gunicorn -w 5 -b 0.0.0.0:${PORT} api_adobe:app"]
