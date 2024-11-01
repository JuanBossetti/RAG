# ej: docker run -d --env-file .env -p 7000:8501 --network community -e PORT=7000 ui

FROM python:3.9-slim-buster

RUN pip install --upgrade pip==20.0.2

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]