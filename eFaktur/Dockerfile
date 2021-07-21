# pull official base image
FROM python:3.8.10

# set work directory
WORKDIR /usr/src/eFaktur

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt-get update \
    && apt-get install -y python3-dev libpq-dev netcat

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# copy migrate_db.sh
COPY ./scripts/migrate_db.sh .

# run entrypoint.sh
ENTRYPOINT ["/usr/src/eFaktur/scripts/migrate_db.sh"]