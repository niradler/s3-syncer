FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV AWS_DEFAULT_REGION us-east-1
ENV AWS_ACCESS_KEY_ID Q4X2N1H22UGQDSK*
ENV AWS_SECRET_ACCESS_KEY KTYTBE125EP3NW3005ZXGYVAYZMEW24*
ADD requirements.txt .
RUN python -m pip install -r requirements.txt

WORKDIR /app
ADD . /app

RUN useradd appuser && chown -R appuser /app
USER appuser

CMD ["python", "sync.py"]
