# Base image
FROM python:latest
LABEL maintainer="VV"
LABEL version="dev"

ENV forkfolder /ilswebprj
WORKDIR ${forkfolder}

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY content/ ${forkfolder}
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:9003", "run:app" ]
# ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:9003", "flaskapp:app" ]
