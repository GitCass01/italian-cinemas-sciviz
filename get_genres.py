import tmdbsimple as tmdb
from utility import *
import json
import os
from dotenv import load_dotenv

load_dotenv()

tmdb.API_KEY = os.getenv('TMDB_API_KEY')

def get_film_genres(ita=True):
    if ita:
        bo = box_offices[box_offices['Naz.'] == 'ITA']
        path='Dati_Cinema_Italiani/tables/film_ita_genres.json'
        print('Inizio ricerca generi per film italiani...')
    else:
        bo = box_offices[box_offices['Naz.'] != 'ITA']
        path='Dati_Cinema_Italiani/tables/film_other_genres.json'
        print('Inizio ricerca generi per film NON italiani...')

    json_file = open(path)
    file = json.load(json_file)

    for index, row in bo.iterrows():
        film = row['Film']

        if film in file:
            continue

        search = tmdb.Search()
        response = search.movie(query=film, language='it-IT')
        try:
            id = search.results[0]['id']
            movie = tmdb.Movies(id)
            genres = movie.info(language='it')['genres']
            file[film] = genres
        except IndexError as e:
            print(film + ' non trovato, anno: ' + str(row['Year']))
    
    json_file.close()
    print('Salvataggio...')
    json_object = json.dumps(file)
    with open(path, "w") as outfile:
            outfile.write(json_object)