FROM python:3

COPY requirements.txt /app/
# /app/ on hakemisto dokcerin sisällä.
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]



