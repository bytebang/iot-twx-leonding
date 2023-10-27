import requests

# Thingworx Einstellungen
THINGWORX_URL = 'https://8cf48.twx.htl.schule/Thingworx/Things/MeinThing/Properties/i1'
HEADERS = {
    'Accept': 'application/json',
    'appkey': '08e5752d-80e5-4efd-aa27-5feb70606f0d'
}

response = requests.get(THINGWORX_URL, headers=HEADERS)

# Überprüfen Sie die Antwort
if response.status_code == 200:
    data = response.json()
    i1_value = data['rows'][0]['i1']
    print(f"i1 Wert: {i1_value}")
else:
    print(f"Fehler beim Abrufen von Daten: {response.text}")
