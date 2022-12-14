import pandas as pd

def combine_csv(root, csvName):
    tmp = []
    for year in range(2005, 2022):
        try:
            df = pd.read_csv(path + str(year) + "/" + csvName, decimal=',', thousands='.', parse_dates=True, dayfirst=True)
        except OSError:
            print('Anno ' + str(year) + ' mancante per: ' + csvName)
            continue
        df['Year'] = year
        for i in range(0, len(df)):
            tmp.append(df.iloc[i])
    df = pd.DataFrame(tmp)
    year_column = df.pop('Year')
    df.insert(0, 'Year', year_column)

    df.to_csv(path + '/' + csvName, index=False)

def init(path="Dati_Cinema_Italiani/tables/"):
    combine_csv(path, 'box_office.csv')                            # FONTE: ANICA
    combine_csv(path, 'nazioni.csv')                               # FONTE: ANICA
    combine_csv(path, 'distribuzioni.csv')                         # FONTE: ANICA
    combine_csv(path, 'mesi.csv')                                  # FONTE: ANICA
    combine_csv(path, 'regioni.csv')                               # FONTE: ANICA
    combine_csv(path, 'film_ita.csv')                              # FONTE: ANICA

path = "Dati_Cinema_Italiani/tables/"
# this create all the csv needed by combining yearly data
# init(path)

box_offices = pd.read_csv(path + 'box_office.csv', sep=',', decimal=',', thousands='.', parse_dates=True, dayfirst=True)
naz = pd.read_csv(path + 'nazioni.csv', sep=',', decimal=',', thousands='.', parse_dates=True, dayfirst=True)
distr = pd.read_csv(path + 'distribuzioni.csv', sep=',', decimal=',', thousands='.', parse_dates=True, dayfirst=True)
mesi = pd.read_csv(path + 'mesi.csv', sep=',', decimal=',', thousands='.', parse_dates=True, dayfirst=True)
regioni = pd.read_csv(path + 'regioni.csv', sep=',', decimal=',', thousands='.', parse_dates=True, dayfirst=True)
film_ita = pd.read_csv(path + 'film_ita.csv', sep=',', decimal=',', thousands='.', parse_dates=True, dayfirst=True)
costo_biglietti = pd.read_csv(path + 'costo_biglietti.csv', sep=',')         # FONTE: SIAE
num_luoghi = pd.read_csv(path + 'num_luoghi.csv', sep=',')                   # FONTE: SIAE
info_cinema = pd.read_csv(path + 'info_cinema.csv', sep=',')                 # FONTE: SIAE

# ritorna la top X dei box office di ogni anno
# X = ultima posizione da prendere dai box office
def get_topX(pos):
    lst = []
    for year in range(2005, 2022):
        for i in range(0, pos):
                lst.append(box_offices[box_offices['Year'] == year].iloc[i])
    top = pd.DataFrame(lst)
    return top

# ritorna il numero di film nella "top" di una determinata "nazione"
def get_naz_top(top, nazione):
    countbynaz = top.groupby(['Year', 'Naz.']).size().to_frame(name='count').reset_index()
    x = countbynaz['Year'].unique()
    naz_top = countbynaz[countbynaz['Naz.'] == nazione]

    naz_years = countbynaz[countbynaz['Naz.'] == nazione]['Year'].tolist()
    for year in range(2005, 2022):
        if year not in naz_years:
            naz_top = pd.concat([naz_top, pd.DataFrame.from_records([{'Year':year, 'Naz.':nazione, 'count':0}])])

    naz_top = naz_top.sort_values(by=['Year'])['count']
    return naz_top