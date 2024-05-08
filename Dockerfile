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

