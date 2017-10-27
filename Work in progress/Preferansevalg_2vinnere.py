# -*- coding: utf-8 -*-
# Når en får to eller flere som vinner.
# Se på andrestemmen de gitte kandidatene for å velge en som vinner.
# Om to eller flere har like mange andrestemmer, gå videre og tell tredjestemmene.

# Siden dette kna skje når so helst må det være dynamisk. Dvs at den som telles over, må se på de _neste_ stemmene på
# de gitte stemmesedlene.

# Om en av de to gjennværende kandidatene ikke har flere stemmer, har den personen tapt.

# Om to eller flere kandidater har like mange stemmer i alle ledd. Velges det med myntkast.

def flere_vinnere(kandidat_over_sperregrense, score, stemmesedler, kandidater):
    valgt_kandidat = 0

    print(kandidat_over_sperregrense)

    secondary_score = []
    for i in range(len(kandidater)):
        secondary_score.append(0)

    temp_pos = len(kandidater) - 1
    stemme_telles = False

    for i in range(len(stemmesedler)):
        for j in range(len(stemmesedler[i])):

            if (stemmesedler[i][j] < stemmesedler[i][temp_pos]) or (stemmesedler[i][temp_pos] < 0):
                if stemmesedler[i][j] >= 0:
                    temp_pos = j
                    stemme_telles = True

        if stemme_telles == True:
            secondary_score[temp_pos] += 1

        # Nullstill for neste stemme
        temp_pos = len(kandidater) - 1
        stemme_telles = False

    #Velg kandidat med flest net høyeste stemmer
    kandidat_over = -1
    print("MAX")
    print(max(secondary_score))


    return valgt_kandidat
