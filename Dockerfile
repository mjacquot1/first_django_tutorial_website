# FROM debian:latest

# RUN apt-get update --fix-missing 

# RUN apt install build-essential \
#     zlib1g-dev \
#     libncurses5-dev \
#     libgdbm-dev \
#     libnss3-dev \
#     libssl-dev \
#     libreadline-dev \
#     libffi-dev \
#     libsqlite3-dev \
#     wget libbz2-dev\
#     -y

# RUN apt install python3 -y

# RUN apt install python3-pip -y

# WORKDIR /usr/src/app

# COPY requirements.txt ./


# RUN pip3 install --no-cache-dir -r requirements.txt

# COPY . .

# WORKDIR "./my_site"

# CMD [ "python", "manage.py", "runserver" ]

FROM python:latest
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
