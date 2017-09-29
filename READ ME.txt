PREFERANSEVALG

Utgangspunkt i beskrivelsen til VT Vest sitt valgreglement.

HVORDAN BRUKE:
1)	Legg alle stemmesedlene som skal telles opp i et excel-dokument med navnet 
	"Stemmesedler.xlsx". Om du er uksikker ligger det et eksempel i denne mappen.
	OBS: Bytt navn paa eksempelet, programmet vil alltid ta filen med navnet
	"Stemmesedler.xlsx" som sin input-fil.

2)	Kjoer "Valgsystem_preferansevalg.py"
	Pass paa at "Valgsystem_preferansevalg.py", "Preferansevalg_imports_v3.py" og
	"Stemmesedler.xlsx" ligger i den samme mappen.

3)	Programmet skal naa opprette "Resultat.xlsx" og "Status.txt"

	"Resultat.xlsx" inneholder alle kandidater med plassering. Du maa mest sannsynlig aapne
	dokumentet og rearrangerer rekkefoelgen. Programmet skirver bare ut kandidatene etterhvert 	som de vinner eller taper i valgsystemet.
	
	"Status.txt" skriver ut hele prosessen, s�aa om det skulle vaere usikkerhet om hva som har
	skjedd er det mulighet til aa gaa over her og kontrollere.


KRAV TIL PYTHON:
Python 3.6

Delprogram du maa laste ned til Python:
	openpyxl
	random
