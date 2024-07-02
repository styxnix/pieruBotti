import discord
import urllib.parse
import json

# JSON-tiedoston nimi
kielletyt_osoitteet_tiedosto = 'kielletytOsoitteet.json'

def lue_linkit():
    """Lue linkit JSON-tiedostosta ja palauta ne listana."""
    with open(kielletyt_osoitteet_tiedosto, 'r') as tiedosto:
        data = json.load(tiedosto)
    return data['kielletyt_osoitteet']

async def autoDeleteMessages(message):
    kielletyt_osoitteet = lue_linkit()

    # Tarkista, jos viestissä on kielletty URL
    for url in kielletyt_osoitteet:
        if url in message.content:
            # Poista viesti
            try:
                await message.delete()
                print(f"Deleted message from {message.author} containing banned URL: {url}")
            except discord.NotFound:
                # Viestiä ei löydy, ei tarvitse tehdä mitään
                pass
            return  # Lopetetaan tarkistus, koska viesti on jo poistettu

    # Tarkista, jos viestissä on kielletty URL osana isompaa tekstiä
    for url in kielletyt_osoitteet:
        parsed_url = urllib.parse.urlsplit(url)
        if parsed_url.geturl() in message.content:
            # Poista viesti
            try:
                await message.delete()
                print(f"Deleted message from {message.author} containing banned URL part: {url}")
            except discord.NotFound:
                # Viestiä ei löydy, ei tarvitse tehdä mitään
                pass
            return  # Lopetetaan tarkistus, koska viesti on jo poistettu
