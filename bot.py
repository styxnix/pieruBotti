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

# Lue asetukset JSON-tiedostosta
def lue_asetukset():
    with open('asetukset.json', 'r') as tiedosto:
        return json.load(tiedosto)

asetukset = lue_asetukset()

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix='!', intents=intents)

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
        logging.info(f"Message sent to {message.author}: {response}")
    except Exception as e:
        logging.error(f"Error occurred while sending message: {e}")

def run_discord_bot():
    botToken = TOKEN

    @client.event
    async def on_ready():
        logging.info(f"{client.user} on nyt käynnissä!")
        # Huomio: Avain "servers" on päivitetty "palvelimet"
        for server_id, config in asetukset['palvelimet'].items():
            channel = client.get_channel(config['ilmoitusKanavaID'])
            if channel:
                await channel.send("Botti pieruvahdissa.")

@client.event
async def on_voice_state_update(member, before, after):
    if before.channel is None and after.channel is not None:
        if member.bot:  # Jos kanavalle liittyy botti, ohita
            return

        guild_id = str(member.guild.id)
        if guild_id in asetukset['palvelimet']:
            channel_name = after.channel.name
            message = f'Jahas, {member.name} on piereskelemässä kanavalla {channel_name}.'
            ilmoitusKanavaID = asetukset['palvelimet'][guild_id]['ilmoitusKanavaID']
            ilmoitus_channel = client.get_channel(ilmoitusKanavaID)
            if ilmoitus_channel:
                await ilmoitus_channel.send(message)
                logging.info(f"Notification sent: {message}")
            else:
                logging.warning("Notification channel not found.")

    client.run(botToken)

run_discord_bot()
