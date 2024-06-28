FROM python:3.9-slim-buster

WORKDIR /app

COPY Pipfile Pipfile.lock ./

# install these dependencies to remediate psycopg2-binary install issue.
# issue was occurring durring linux/arm64 docker build.
RUN apt-get update \
&& apt-get -y install libpq-dev gcc \
&& pip install psycopg2

RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY . .

EXPOSE 5000

ENV FLASK_APP=application.py

CMD ["pipenv", "run", "gunicorn", "-b", "0.0.0.0:5000", "application:application"]

# FOR LOCAL DEVELOPMENT
# CMD ["pipenv", "run", "flask", "run", "--host=0.0.0.0"]
