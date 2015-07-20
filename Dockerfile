# Dockerfile extending the generic Python image with application files for a
# single application.
FROM gcr.io/google_appengine/python-compat
RUN yes | pip install flask
ADD . /app
