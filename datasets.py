import pandas as pd
import glob

def combine_csv(root, csvName):
    box_office = []
    for year in range(2005, 2022):
        try:
            df = pd.read_csv(path + str(year) + "/" + csvName, decimal=',', thousands='.', parse_dates=True, dayfirst=True)
        except OSError:
            print('Anno ' + str(year) + ' mancante per: ' + csvName)
            continue
        df['Year'] = year
        for i in range(0, len(df)):
            box_office.append(df.iloc[i])
    df = pd.DataFrame(box_office)
    year_column = df.pop('Year')
    df.insert(0, 'Year', year_column)
    return df

path = "Dati_Cinema_Italiani/tables/"                                        # FONTE: ANICA
box_offices = combine_csv(path, 'box_office.csv')                            # FONTE: ANICA
naz = combine_csv(path, 'nazioni.csv')                                       # FONTE: ANICA
distr = combine_csv(path, 'distribuzioni.csv')                               # FONTE: ANICA
mesi = combine_csv(path, 'mesi.csv')                                         # FONTE: ANICA
regioni = combine_csv(path, 'regioni.csv') # mancano dati dal 2018 in poi    # FONTE: ANICA
film_ita = combine_csv(path, 'film_ita.csv')                                 # FONTE: ANICA
costo_biglietti = pd.read_csv(path + 'costo_biglietti.csv', sep=',')         # FONTE: SIAE
num_luoghi = pd.read_csv(path + 'num_luoghi.csv', sep=',')                   # FONTE: SIAE
info_cinema = pd.read_csv(path + 'info_cinema.csv', sep=',')                 # FONTE: SIAE