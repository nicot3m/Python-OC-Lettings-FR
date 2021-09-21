# Set base image (host OS)
FROM python:3.8

# Setup the working directory in the container
WORKDIR /code

# Define the usable volume
VOLUME /code

# Setup environment variables
# Prevent from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
# Display output w/o bufferin
ENV PYTHONUNBUFFERED 1
ENV PORT=8000

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code
RUN pip install -r requirements.txt

# Copy project to code
COPY . /code

# Define the default port and block access for other applications
EXPOSE $PORT

# Collect static
RUN python manage.py collectstatic --noinput

# Setup the executable command in the container
CMD python manage.py runserver 0.0.0.0:$PORT