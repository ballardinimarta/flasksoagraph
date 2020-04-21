FROM python:3.8-slim-buster
RUN apt-get update && \
    apt-get install --no-install-recommends -y gcc && \
    apt-get clean && rm -rf /var/lib/apt/lists/*
COPY flaskapp /flaskapp
COPY requirements.txt /flaskapp
WORKDIR /flaskapp
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
