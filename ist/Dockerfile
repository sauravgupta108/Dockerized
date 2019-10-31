# Python 3.6 as base image
From python:3.6

ENV PYTHONPATH /usr/local/lib/python3.6/site-packages

# Create directory for code inside container and go to that directory.
RUN mkdir -p /opt/app/code/ist
WORKDIR /opt/app/code/ist

# Install all requirements as listed in requirements.txt file 
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy project files to container
COPY . .
EXPOSE 7000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:7000"]
