FROM python:3.7.2

COPY . /lnkd

WORKDIR lnkd

RUN pip install -r requirements.txt

RUN python setup.py install
