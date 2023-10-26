# Author: Jaakko Saarikko

import discord
import responses
import deleteMessages
from botToken import TOKEN

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

    @client.event
    async def on_message(message):
        if message.author == client.user:
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

