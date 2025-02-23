FROM python:3.9.1-alpine3.12

RUN pip install flask

WORKDIR /app
COPY echo.py .
RUN chmod u+x echo.py

CMD [ "python", "./echo.py"]