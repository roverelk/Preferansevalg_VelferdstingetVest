def tekst(x):
    return {
        '1': 'Dette programmet leser inn et excel-ark for så å fortelle deg hvem som har vunnet!',
        '2': 'Trolololol',
        'Button1': 'Regn ut valg',
        'Button2': 'Lag eksempel',
        'Button3': 'Preferansevalg?',
        'Button4': 'Donér',
        'Menu1': '&Fil',
        'Menu2': '&Hjelp',
        'Menu3': '&Om'
    }.get(x, 'ERROR: TEXT NOT FOUND')