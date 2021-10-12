FROM python:3.7.1

LABEL Author="{{cookiecutter.Author}}"
LABEL E-mail="{{cookiecutter.Email}}"
LABEL version="{{cookiecutter.Version}}"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "{{cookiecutter.project_name}}/app/app.py"
ENV FLASK_ENV "development"
ENV FLASK_DEBUG True

RUN mkdir /app
WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0