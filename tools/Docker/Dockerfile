# Base image
FROM python:latest
LABEL maintainer="VV"
LABEL version="dev"

ENV forkfolder /app
WORKDIR ${forkfolder}

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /tmp/requirements.txt

COPY content/ ${forkfolder}

ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:9003", "flaskapp:app" ]