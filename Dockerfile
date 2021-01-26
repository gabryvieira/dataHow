FROM python:3.5.2

COPY ./ ./

RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "main.py"]