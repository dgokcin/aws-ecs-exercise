FROM python:3-alpine

ARG REQUIREMENTS="python3-dev build-base linux-headers pcre-dev gcc"

RUN apk update &&\
    apk add ${REQUIREMENTS}

# Set application working directory
WORKDIR /usr/src/app

# Expose 5000th port
EXPOSE 5000

# Install requirements
COPY webapp/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install application
COPY webapp/app.py .

# Run application
CMD ["python3", "./app.py"]
