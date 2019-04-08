FROM python:3.5.7

RUN pip install iofog-python-sdk ws4py

COPY . .

ENTRYPOINT ["python3", "webconsumer.py"]