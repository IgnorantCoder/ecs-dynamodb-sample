FROM python:3-alpine

WORKDIR /tmp

ADD requirements.txt ./
ADD constraints.txt ./
ADD main.py ./

RUN pip install -r requirements.txt -c constraints.txt

EXPOSE 8000

CMD ["gunicorn", "main:app", "-b", "0.0.0.0:8000", "--access-logfile", "-"]