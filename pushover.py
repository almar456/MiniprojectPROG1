import http.client, urllib                                          #urlib en http.client importen
def pushover_send(username):                                        # functie om pushover berichten te sturen (pushover api)
    readfile = open('fietsen.csv', 'r').readlines()
    for regel in readfile:
        lijst = regel.split(';')
        if username == lijst[2]:
            user_code = lijst[6]
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": "ajzuvap1nro2679gr3i1o8ntvkahv7",
        "user": user_code,
        "message": "Uw heeft zojuist uw fiets opgehaald.",
      }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
