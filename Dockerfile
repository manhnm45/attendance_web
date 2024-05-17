FROM python:3

WORKDIR /manage

COPY requirement.txt .

RUN pip3 install -r requirement.txt



COPY . .
EXPOSE 8000
CMD ["python3", "manage.py","runserver","0.0.0.0:8000"]

