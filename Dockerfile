FROM python:3.10.2-slim

WORKDIR /var/www

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update || : && apt-get install -y \
    python \
    build-essential \
    gettext \
    libgettextpo-dev \
    libcurl4-openssl-dev \ 
    libssl-dev \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install --upgrade pip

RUN pip uninstall pycurl
RUN pip install pycurl --compile --global-option="--with-openssl" --no-cache-dir

RUN pip install --upgrade pipenv gunicorn
RUN pipenv install --system --deploy

COPY . .
RUN chmod +x ./.docker/entrypoint.sh

ARG _SECRET_KEY='^p5f!4x3f72i&lsma!-n9y7m2j0bf)n$g6(yy_+*fmgp3sc)-#'
ENV SECRET_KEY=$_SECRET_KEY
ARG _DJANGO_ALLOWED_HOSTS=localhost;127.0.0.1;[::1]
ENV DJANGO_ALLOWED_HOSTS=$_DJANGO_ALLOWED_HOSTS

RUN python manage.py collectstatic --noinput

ENTRYPOINT ["sh", "./.docker/entrypoint.sh"]