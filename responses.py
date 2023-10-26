import random
import deleteMessages

kielletyt_sanat = ["neekeri", "neek3ri", "n33k3ri", "n33k3r1", "neek eri", "nigger", "n1gger",  "nigga", "n1gga", "neger", "n3g3r"]

def get_response(message) -> str:
    p_message = message.lower()

    if p_message == "testi":
        return "`Tämä on testiviesti`"

    if  p_message ==  "`noppa`":
        return str(random.randint(1, 6)) 

    if p_message == "ohjeet":
        return "`Tässä ohjeet Botin komentamiseen: `"

def banned_words(user_message):
    for sana in kielletyt_sanat:
        if sana in user_message:
            return True
        elif len(sana) == len(user_message) and sum(a != b for a, b in zip(sana, user_message)) <= 2:
            return True
    return False

