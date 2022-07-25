README.md

# MQTT-exempel1
Publicerar meddelanden inmatade från terminalen och skriver ut dessa efter mottagande via host "broker.hivemq.com". 

Filen client.py används för att publicera meddelanden, där inmatning sker från terminalen tills användaren matar in en tom rad.
Meddelanden publiceras till topic "python/mqtt/topics/topic1".
 
Filen server.py används för att ta emot meddelanden från alla topics som börjar med "python/mqtt/topics" via ett wildcard. Varje mottaget meddelande skrivs ut tillsammans med topic det togs emot från.

Starta filerna var sin enhet, exempelvis client.py på Ubuntu och server.py i Visual Studio 2022 eller på din Raspberry Pi.

Kommentarer har skrivits på engelska, då Python för Visual Studio 2022 inte stödjer å, ä och ö i flerradiga kommentarer. Det fungerar dock ifall C-style
kommentarsblock används, men dokumentation i funktioner, klasser med mera skall göras med """ Detta är en flerradig kommentar. """

