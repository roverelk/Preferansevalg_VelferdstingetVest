# Preferansevalg for Velferdstinget Vest <img src="https://pbs.twimg.com/profile_images/892342855943036928/YBSKHYbA_400x400.jpg" width="200" height="200" align="right">

## Hvordan bruke
Dette programmet tar stemmesedler lagt inn i et excel-ark og returnerer en liste over hvem som kom i hvilke plassering.

Det er dynamisk som betyr at du kan forandre antall kandidater og antall stemmer og programmet vil fredmeles gjennomføre valget for deg.

## Last ned herfra
Last ned:
1. Klikk "Clone or Download"
2. Pakk ut zip
3. Velg den mappen du trenger: "Run on Windows" eller "Run on MAC". Resten trenger du ikke.
4. Inne i den mappen liger alt du trenger, sammen med et eksempel

## Kjør test
Om du allerede har `Python 3.6` og `openpyxl` installert kan du kjøre en test for å se om alt virker. Hvis ikke gå ned til [Last ned fra andre steder](https://github.com/roverelk/Preferansevalg_VelferdstingetVest#last-ned-fra-andre-steder).

### Hvordan kjøre test
1. Pass på at Preferansevalg.py, Preferanseval_vedlegg.py og Stemmesedler.xslx ligger i samme mappe.
2. Dobbelklikk på Preferansevalg.py for å starte det.
3. Det skal nå opprettes to nye filer: Resultat.xslx og Status.txt
4. Gratulerer alt virker!

## Instalasjonsguide for Windows
Du trenger Python for å kunne kjøre programfilene.
### Python 3.6
Last ned: [Python 3.6.3](https://www.python.org/ftp/python/3.6.3/python-3.6.3.exe "This is a direct donwload link :-)")

### Plugins til Python 3.6
I tillegg til Python 3.6 trenger du et tillegg for å kunne lese tall fra excel-ark.
#### `openpyxl`
1. Åpne "command prompt", også kjent som "ledetekst"
2. Skriv inn `pip3 install openpyxl`
3. Trykk Enter
4. Nå skal `openpyxl` laste seg ned og installeres, det vil stå masse fin forklarende tekst på skjermen
