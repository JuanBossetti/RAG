#Para crear esta imagen se debe definir puerto interno de api con la variable de entorno PORT, y su volumen de modelos (internamente deberia pegar a /app/models)
# ej: docker run -d -p 5000:7000 -e PORT=7000 -v /mnt/datos/desarrollo/huggingface-models:/app/models question-app
# ej: docker run -d --env-file .env -p 8002:7000 --network community -e PORT=7000 -v /mnt/datos/desarrollo/huggingface-models:/app/models chat
# Hay que especificar la ruta absoluta del volumen (/mnt/datos/desarrollo/huggingface-models)

FROM python:3.9-slim-buster

RUN pip install --upgrade pip==20.0.2

RUN apt-get update && apt-get install -y \
    patchelf \
    ninja-build \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /app/models

WORKDIR /app

RUN HF_HOME=/app/models/

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Comando para verificar si la variable de entorno PORT está definida y ejecutar la aplicación
CMD ["sh", "-c", "if [ -z \"$PORT\" ]; then echo 'Error: PORT variable is not set'; exit 1; fi; flask run --host=0.0.0.0 --port=${PORT}"]