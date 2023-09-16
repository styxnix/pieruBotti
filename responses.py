import random
import deleteMessages

kielletyt_sanat = ["neekeri", "nigger", "n1gger", "n33k3ri", "n33k3r1", "nigga", "n1gga", "neger", "n3g3r"]

def get_response(message) -> str:
    p_message = message.lower()

    if p_message == "testi":
        return "`Tämä on testiviesti`"

    if  p_message ==  "`noppa`":
        return str(random.randint(1, 6)) 

    if p_message == "ohjeet":
        return "`Tässä ohjeet Botin komentamiseen: `"

    if p_message in kielletyt_sanat:
        return "`Käyttämäsi sana on kiellettyjen sanojen listalla.`"        

    if deleteMessages():
        return "`Viestisi on kielletty, koska ketään ei vittu kiinnosta se, joten lopeta.`"