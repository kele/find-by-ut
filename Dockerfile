# Dockerfile extending the generic Python image with application files for a
# single application.
FROM gcr.io/google_appengine/python-compat
RUN apt-get update && apt-get install -y git
RUN mkdir /codebase
RUN git clone https://github.com/python-git/python.git /codebase/python
RUN yes | pip install flask
ADD . /app
ENV PYTHONPATH=/app
