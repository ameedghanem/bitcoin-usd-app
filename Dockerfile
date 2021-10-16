FROM python:3.8

COPY requirements.txt ./

RUN pip install -r requirements.txt

#ENV PYTHONPATH ./bitcoin/bitcoinprice

COPY . ./

CMD ["python3", "web.py"]
