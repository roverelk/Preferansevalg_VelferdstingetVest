def tekst(x):
    return {
        '1'         : 'Dette programmet leser inn et excel-ark for så å fortelle deg hvem som har vunnet!',
        '2'         : 'Trolololol',
        'Button1'   : 'Regn ut valg',
        'Button2'   : 'Lag eksempel',
        'Button3'   : 'FAQ',
        'Button4'   : 'Donér',
        'Menu1'     : 'Fil',
        'Menu2'     : 'Hjelp',
        'Menu3'     : 'Om',

        'Menu2_text': 'Regn ut valg'
                      '\n- Legg alle stemmer inn i excel-arket ditt.'
                      '\n- Klikk på \'Regn ut valg\''
                      '\n- Gi programmet excel-arket'
                      '\n- Det skal nå være opprettet en mappe med en kopi av excel-arket med stemmesedlene dine sammen'
                      ' med \'Resultater\' (Oversikt over alle kandidater og deres rangering) og \'Sattus\' (Oversikt'
                      ' over hele prosessen og alle avgjørelser som er tatt).'
                      '\n\nFAQ'
                      '\nLink til FAQ på GitHub.'
                      '\n\nLag eksempel'
                      '\nDu kan opprette tre forskjellige eksempler på hvordan excel-arket vil se ut. Så vil'
                      ' programmet regner så ut svarene basert på det sammme som vil skje om en trykker på'
                      ' \'Regn ut valg\''
                      '\n\nDonér'
                      '\nLink til GitHub, mulighet til å gi meg en krone om du liker programmet ;-)',

        'Menu3_text': 'Preferansevalg (a.k.a. Single Transferable Vote)',

        'Button3_clicked': 'FAQ er klikket.\n\nDet skal ha åpnet en link, hvis ikke trykk her:'
                           '<a href="where/you/want/the/link/to/go">text of the link</a>'

    }.get(x, 'ERROR: TEXT NOT FOUND')

def posisjoner(x):
    return{
        'Vindu_h'   : 600,
        'Vindu_b'   : 500,
        'Knapp_h'   : 50,
        'Knapp_b'   : 220,
        'Marg_h'    : 20,
        'Marg_b'    : 20,
        'Marg_topp' : 50
    }.get(x, 'ERROR: MEASURMENT NOT FOUND')