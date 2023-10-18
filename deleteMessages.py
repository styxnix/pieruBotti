async def autoDeleteMessages(message):
    # Auto delete unwanted messages
    # Check if message has attachments
    if message.attachments:
        # Check all attachments
        for attachment in message.attachments:
            # Check attachment filename
            if attachment.filename == 'IMG_1960.gif':  # Image, you want to delete
                # Delete message
                await message.delete()
                break  # Voit lopettaa silmukan, kun poistat ensimmäisen osuman
    # Check if message text contains a specific URL
    elif 'https://media.discordapp.net/attachments/1129134994862903328/1146085397995208795/IMG_1960.gif' in message.content:
        # Delete message
        await message.delete()
