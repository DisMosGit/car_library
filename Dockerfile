FROM python:3.9

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /django
WORKDIR /django

COPY . .
RUN pip install 'pipenv==2018.11.26'
RUN pipenv install --system --deploy --ignore-pipfile
RUN python manage.py makemigrations
RUN python manage.py migrate



EXPOSE 8000
