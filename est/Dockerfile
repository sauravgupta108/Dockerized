# Python 3 as base image
FROM python:3.6

ENV PYTHONPATH /usr/local/lib/python3.6/site-packages

# Create directory inside container for code
RUN mkdir -p /opt/app/code/est
RUN mkdir /opt/app/code/logs
WORKDIR /opt/app/code/logs
RUN touch access.log error.log static-access.log
WORKDIR ../est

# Copy requirements.txt file for requirements to install
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project files to container
COPY . /opt/app/code/est/

EXPOSE 7500

CMD ["python3", "manage.py", "runserver", "0.0.0.0:7500"]
