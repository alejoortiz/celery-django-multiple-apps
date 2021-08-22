FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /var/log/app && mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY ./code /code/
RUN chmod 777 docker-entrypoint.sh
CMD /code/docker-entrypoint.sh