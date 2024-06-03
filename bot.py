# Author: Jaakko Saarikko

import discord
import responses
import deleteMessages
from discord.ext import commands
from botToken import TOKEN
import psutil
import platform
import socket

client = commands.Bot(command_prefix='!')

async def send_message(message, user_message, is_private):
    try:
        response = responses.get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(f"Virhe tapahtui: {e}")

def run_discord_bot():
    botToken = TOKEN
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} on nyt käynnissä!")
#        await client.get_channel(1151586912482644038).send("Botti pieruvahdissa.")

    @client.event
    async def on_voice_state_update(member, before, after):
        if before.channel is None and after.channel is not None:
            if member.id == 944016826751389717: # Jos käyttäjä on musiikkibotti Lara
                return
            channel_name = after.channel.name
            message = f'Jahas, {member.name} on piereskelemässä kanavalla {channel_name}.'
            ilmoitus_channel_id = 1191748814558724156
            ilmoitus_channel = client.get_channel(ilmoitus_channel_id)
            if ilmoitus_channel:
                await ilmoitus_channel.send(message)
            else:
                print("Notification channel not found.")  # Testituloste

    @client.event
    async def on_message(message):
        if message.author == client.user:   # Jos viestin lähettäjä on botti itse, älä tee mitään.
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

    #    print(f'{username} sanoi:"{user_message}" (kanavalla: {channel})')

        if user_message and user_message[0] == "?":
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            if responses.banned_words(user_message):
                response = "Sana on kiellettyjen sanojen listalla."
                await message.channel.send(response)
            else:
            # Suorittaa deleteMessages koodia  
                await deleteMessages.autoDeleteMessages(message)
        

    client.run(botToken)
