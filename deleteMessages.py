import discord
import urllib.parse

async def autoDeleteMessages(message):

    kielletyt_osoitteet = ["https://media.discordapp.net/attachments/1129134994862903328/1146085397995208795/IMG_1960.gif",
"https://media.discordapp.net/attachments/889648627998396467/958347280522571776/20220209_020937.gif",
"https://media.discordapp.net/attachments/889648627998396467/958347280522571776/20220209_020937.gif",
"https://media.discordapp.net/attachments/934628911227215882/951126813294350336/image0-1-1.gif?width=810&height=635",
"https://media.discordapp.net/attachments/625245407122948106/1025368565605474304/r1.gif",
"https://images-ext-1.discordapp.net/external/rZ7Xffd9DD_BtTNJ4U3RL-s05QOpCsWBCZTQbF1ENWo/%3Fcid%3D73b8f7b10rwdt1waoulw1t3bo485bq9wek3gm9i823mtdk61%26ep%3Dv1_gifs_gifId%26rid%3Dgiphy.mp4%26ct%3Dg/https/media1.giphy.com/media/gXXEAd29WXpxsml8Cy/giphy.mp4",
"https://giphy.com/gifs/ww-gXXEAd29WXpxsml8Cy",
"https://images-ext-2.discordapp.net/external/VTQoUnwoAAzXGbnMpNnP7hTKE40za_L9OaQxaurOvS0/https/media.tenor.com/4goyEL9CgwUAAAPo/twenty-century-fox-meme-gfy.mp4",
"https://tenor.com/view/twenty-century-fox-meme-gfy-go-fuck-yourself-meme-get-lost-gif-26260205",
"https://media.discordapp.net/attachments/864780983487954965/1021706609916915763/EDC89514-01C9-4C7D-AA2A-516FD6AE8CDE.gif",
"https://images-ext-1.discordapp.net/external/viWHuNgWLMAp4x56vnav-wtQJ_mWsokvw5vRhhmKTPk/%3Fcid%3D73b8f7b1bbgoje8bf4yh0vd1ziuhi9uxg75f6pnxukgyktgp%26ep%3Dv1_gifs_gifId%26rid%3Dgiphy.mp4%26ct%3Dg/https/media0.giphy.com/media/la9vclufqEVz54YjpR/giphy.mp4",
"https://media.giphy.com/media/la9vclufqEVz54YjpR/giphy.gif"
"https://media.discordapp.net/attachments/889648627998396467/958347280522571776/20220209_020937.gif",
"https://media.discordapp.net/attachments/1030920325262745620/1104816106855731320/7kveo6.gif",
"https://media.discordapp.net/attachments/934665287339499560/969753529810034718/kowalski.gif",
"https://media.discordapp.net/attachments/934628911227215882/951126813294350336/image0-1-1.gif?width=810&height=635",
"https://media.discordapp.net/attachments/934628911227215882/951126813294350336/image0-1-1.gif",
"https://media.giphy.com/media/la9vclufqEVz54YjpR/giphy.gif",
"https://images-ext-1.discordapp.net/external/viWHuNgWLMAp4x56vnav-wtQJ_mWsokvw5vRhhmKTPk/%3Fcid%3D73b8f7b1bbgoje8bf4yh0vd1ziuhi9uxg75f6pnxukgyktgp%26ep%3Dv1_gifs_gifId%26rid%3Dgiphy.mp4%26ct%3Dg/https/media0.giphy.com/media/la9vclufqEVz54YjpR/giphy.mp4",
"https://images-ext-2.discordapp.net/external/-O_-P5ym_uHtnKWNU0CK13i-6n0E4F2MEVqn1spm7-M/https/media.tenor.com/pw426ez7qM8AAAPo/jee-jee-jee-jee-jee-jee-rock-rock-rock-kohta-p%25C3%25A4%25C3%25A4see-r%25C3%25B6%25C3%25B6kille-ja-naiselle.mp4",
"https://media.discordapp.net/attachments/879122843160440903/923982054314635364/image0.gif",
"https://media.discordapp.net/attachments/508392234291560458/1071369881670389821/79xm7c.gif",
"https://media.discordapp.net/attachments/870210769478885377/885827784566525962/cry_about_it.gif",
"https://media.discordapp.net/attachments/911037876391796766/1009490757008240732/kill_button_bruh.gif",
"https://media.discordapp.net/attachments/758434041526878214/1076130834349826058/IMG_0506.gif?width=750&height=600",
"https://images-ext-1.discordapp.net/external/ayulH8Hmc3NqsNQPQRURwP2bJQdSjJnjkP5RtDnAfi0/%3Fcid%3D73b8f7b1wn42fs2fm8jupsbi4b7cmd5b540pvckyid2aarcn%26ep%3Dv1_gifs_gifId%26rid%3Dgiphy.mp4%26ct%3Dg/https/media0.giphy.com/media/kWxAUxpWVhnuo4uEHm/giphy.mp4",
"https://media0.giphy.com/media/kWxAUxpWVhnuo4uEHm/giphy.mp4?cid=73b8f7b1ea9db62baf8c012973a71d2b0dccdacb3a281431&rid=giphy.mp4&ct=g" ]

    # Check if message text contains a specific URL
    for url in kielletyt_osoitteet:
        if url in message.content:
            # Delete message
            try:
                await message.delete()
            except discord.NotFound:
                # Viestiä ei löydy, ei tarvitse tehdä mitään
                pass

    # Tarkista, jos viestissä on kielletty URL
    for url in kielletyt_osoitteet:
    # Erotetaan URL-osoite tekstistä
        parsed_url = urllib.parse.urlsplit(url)
    
        if parsed_url.geturl() in message.content:
            # Poista viesti
            try:
                await message.delete()
            except discord.NotFound:
                # Viestiä ei löydy, ei tarvitse tehdä mitään
                pass
