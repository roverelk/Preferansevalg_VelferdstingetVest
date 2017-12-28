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


HVORDAN PROGRAMMET VIRKER

1) Legg alle stemmene inn i excel-arket "Stemmesedler"
2) Lagre Stemmesedler.xlsx i samme mappe som valgprogrammet ligger
3) Start valgprogrammet
4) Programmet leser inn alle stemmene som er lagt i excel-arket.
5) Det finner:
	Antall stemmesedler
	Antall kandidater som stiller

6) Sett sperregrensen:
	([Ant stemmesedler] / [Ant kandidater]) + 0.01 = Sperregrense

7) Tell opp antall førstestemmer hver kandidat har fått

8) Ta avgjørelser på hvem som har vunnet / tapt
	8a) Noen har vunnet
		8aa) Flere enn en person har vunnet.*
		     Tell andrestemmen til alle som stiller likt til å vinne, den med flest andrestemmer vinner.*
		     Om ingen får andrestemmen, telles tredjestemmen, osv...
		     Om en kandidat går tom for stemmer, har personen tapt fremfor en kandidat som får stemmer.
		     Om det fremdeles er uavgjort blir det gjennomført med myntkast.*
		     Kandidat som har vunnet blir annonsert.*

		8ab) Bare en kandidat har vunnet.
		     Kandidat som har vunnet blir annonsert.*

	    En finner alle stemmesedeler som har kandidaten som sin vinner. Teller opp hvor de fordeler sin neste stemme,
	    og fordeler dem etter:

		([Antall stemmer kandidaten fikk]-[Sperregrensen])*[Neste prioritert på stemmeseddel]
		= [Fordeles ut til de andre kandidatene]

	    Det fordeles bare stemmer til kandidater som er igjen, og som ikke har hverken vunnet eller tapt.


	8b) Noen har tapt
	    En teller opp alle de neste stemmene på stemmesedlene deres.
	    Stemme fordeles til de gjennværende kandidatene som ikke har hverken vunnet eller tapt.
