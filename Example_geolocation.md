## Geolocation Beispiel

Anleitung basierend auf 

https://community.ptc.com/t5/IoT-Tips/Display-Geolocation-Data-Using-Google-Maps-Part-1/ta-p/829095

- Extension installieren.
- Google Maps API Key generieren https://console.cloud.google.com/google/maps-apis
- Key wie in der Anleitung oben beschrieben einstellen.



## Eigene GPS Daten nach Thingworx senden.

Es können eigene GPS Daten vom Smartphone über MQTT an eine TWX Instanz gesendet werden. Zum Beispiel mit der App OwnTracks. 

https://play.google.com/store/apps/details?id=org.owntracks.android&hl=de_AT&gl=US

https://apps.apple.com/de/app/owntracks/id692424691

## Thingworx Todos

#### 1 MQTT Connection anlegen

- Things -> new -> Mqtt Connection. 
- Unter Configuration den dementsprechenden MQTT Broker eintragen.

#### 2 MQTT Subscriber Thing anlegen

- Property vom Typ JSON für die Rohdaten anlegen.

- Unter Configuration ein Mapping zwischen dem MQTT Topic und den Rohdaten eintragen.

- Property vom Typ Location für die geparsten Location Daten anlegen.

- Subscription anlegen. DataChange -> rawLocationData

  ````javascript
  me.locationData = {
      latitude: me.rawLocationData.lat,
      longitude: me.rawLocationData.lon,
      elevation: 0,
      units: "WGS84"
  };
  ````

#### 3 Mashup anlegen

- Google Maps Widget in den Mashup ziehen.
- Unter Data das Location Thing auswählen und das Service GetPropertyValues anzeigen.
- All Data mit Drag and Drop auf das Maps Widget ziehen. Dort Data auswählen.
- In den Properties des Google Maps Widgets bei Location Field die Location Data auswählen.
- Die aktuellen Standortdaten sollten jetzt im Mashup angezeigt werden.





