<<<<<<< HEAD
FROM python:3

COPY requirements.txt /app/
# /app/ on hakemisto dokcerin sisällä.
WORKDIR /app
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]


=======
FROM python:3.9

# Luo ja siirry /app-hakemistoon
WORKDIR /app

# Kopioi projektisi tiedostot /app-hakemistoon
COPY . /app

# Luo ja aktivoi virtualenv
RUN python -m venv venv
# RUN /bin/bash -c "source venv/bin/activate"

# Asenna projektin riippuvuudet
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Määritä Dockerin käyttämä komento (tässä vaiheessa voi olla esimerkiksi botin käynnistävä komento)
CMD ["venv/bin/python", "./main.py"]
>>>>>>> facc905e6863b1c09fa100ad57b3ccce62d50943

