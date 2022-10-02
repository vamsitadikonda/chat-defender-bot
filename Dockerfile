FROM python:3

WORKDIR /app

COPY . .

RUN python3 -m pip install -r requirements.txt

CMD python -u ./code/run.py