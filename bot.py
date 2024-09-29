"""
PieruBotti

Author: Jaakko Saarikko

This bot interacts with Discord to perform various tasks including message handling,
automated message deletion based on content, and logging.

Libraries used:
- discord: Provides functionality for interacting with the Discord API.
- discord.ext.commands: Facilitates creation of commands for the Discord bot.
- responses: Sisältää funktioita, joita tarvitaan botin vastauksen muodostamiseen käyttäjän viestien perusteella.
- deleteMessages: Implements functions for automatically deleting messages containing
  prohibited content.
- botToken: Imports the bot's token for authentication with the Discord API.
- psutil: Provides system and process utilities (used for system information).
- platform: Provides access to underlying platform's identifying data (used for system information).
- socket: Provides low-level networking interfaces (potentially used for advanced networking tasks).
- logging: Tarvitaan lokituksen toimintaan.
"""

import discord
from discord.ext import commands
import responses
import deleteMessages
from botToken import TOKEN
import psutil
import platform
import socket
import logging
import json

# Lokituksen konfiguraatio
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler()
    ]
)

# Lataa asetukset tiedostosta
def load_settings():
    try:
        with open('asetukset.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("asetukset.json tiedostoa ei löytynyt.")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"Virhe luettaessa asetuksia: {e}")
        return {}

settings = load_settings()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        logging.info(f"Lähetettiin viesti {message.author}: {response}")
    except Exception as e:
        logging.error(f"Virhe tapahtui viesti lähettäessä: {e}")

def run_discord_bot():
    botToken = TOKEN

    @client.event
    async def on_ready():
        logging.info(f"{client.user} pierubotti on nyt käynnissä!")

        for guild_id, guild_settings in settings.get("kanavat", {}).items():
            ilmoituskanava_id = guild_settings.get("ilmoituskanava_id")
            ilmoituskanava = client.get_channel(ilmoituskanava_id)
        
        if ilmoituskanava is not None:
            await ilmoituskanava.send(f"Botti pieruvahdissa palvelimella {guild_id}.")
        else:
            logging.warning(f"Ilmoituskanavaa ei löytynyt palvelimella {guild_id}. Tarkista asetukset.")

    @client.event
    async def on_voice_state_update(member, before, after):
        if before.channel is None and after.channel is not None:
            if member.bot:  # Jos kanavalle liittyy botti, älä tee mitään
                return

            # Hae palvelimen ID ja liittyvän puhekanavan nimi
            guild_id = str(after.channel.guild.id)
            puhekanava_nimi = after.channel.name

            # Hae palvelimen asetukset
            guild_settings = settings.get("kanavat", {}).get(guild_id)

            if guild_settings:
                # Hae ilmoituskanavan ID asetuksista
                ilmoituskanava_id = guild_settings.get("ilmoituskanava_id")
                ilmoituskanava = client.get_channel(ilmoituskanava_id)

                if ilmoituskanava:
                    message = f'Jahas, {member.name} on liittynyt puhekanavalle {puhekanava_nimi}.'
                    await ilmoituskanava.send(message)
                    logging.info(f"Ilmoitus lähetetty: {message}")
                else:
                    logging.warning(f"Ilmoituskanavaa ei löytynyt palvelimelta {guild_id}.")
            else:
                logging.warning(f"Asetuksia ei löytynyt palvelimelle {guild_id}.")

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        # Lokitetaan käyttäjän viestit
        logging.info(f"Message from {username} in {channel}: {user_message}")

        if user_message and user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            if responses.banned_words(user_message):
                response = "Sana on kiellettyjen sanojen listalla."
                await message.channel.send(response)
                logging.info(f"Banned word detected in message from {username}")
            else:
                await deleteMessages.autoDeleteMessages(message)

    client.run(botToken)

run_discord_bot()
