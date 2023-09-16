async def autoDeleteMessages(message):
    
    # Auto delete unwanted messages

    # Check if message has attachments
        if message.attachments:
        # Check all attachments
            for attachment in message.attachments:
            # Check attachement filename
                if attachment.filename == 'IMG_1960.gif':  # Image, you want to delete
                # Delete message
                    await message.delete()
                    break  # Voit lopettaa silmukan, kun poistat ensimmäisen osuman