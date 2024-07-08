import random
import json

# JSON-tiedoston nimi
kielletyt_osoitteet_tiedosto = 'kielletytOsoitteet.json'

def lue_kielletyt_sanat():
    with open(kielletyt_osoitteet_tiedosto, 'r') as tiedosto:
        data = json.load(tiedosto)
    return data.get('kielletyt_sanat', [])

def get_response(message) -> str:
    p_message = message.lower()

    if p_message == "testi":
        return "`Tämä on testiviesti`"

    if p_message == "`noppa`":
        return str(random.randint(1, 6))

    if p_message == "ohjeet":
        return "`Tässä ohjeet Botin komentamiseen: `"

def banned_words(user_message):
    kielletyt_sanat = lue_kielletyt_sanat()
    for sana in kielletyt_sanat:
        if sana in user_message:
            return True
        elif len(sana) == len(user_message) and sum(a != b for a, b in zip(sana, user_message)) <= 2:
            return True
    return False
