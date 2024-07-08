# deleteMessages.py

import discord
import urllib.parse
import json
import logging

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
            try:
                await message.delete()
                logging.info(f"Deleted message from {message.author} containing banned URL: {url}")
            except discord.NotFound:
                pass
            return

    # Tarkista, jos viestissä on kielletty URL osana isompaa tekstiä
    for url in kielletyt_osoitteet:
        parsed_url = urllib.parse.urlsplit(url)
        if parsed_url.geturl() in message.content:
            try:
                await message.delete()
                logging.info(f"Deleted message from {message.author} containing banned URL part: {url}")
            except discord.NotFound:
                pass
            return
