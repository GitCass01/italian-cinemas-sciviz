import collections
import tmdbsimple as tmdb
from utility import *
import json
import os
from dotenv import load_dotenv

load_dotenv()

tmdb.API_KEY = os.getenv('TMDB_API_KEY')

def get_film_genres(ita=True, all=False):
    if all:
        bo = box_offices
        path='Dati_Cinema_Italiani/tables/film_all_genres.json'
        print('Inizio ricerca generi per tutti i film...')
    elif ita:
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
            for i in search.results:
                if film.lower() == i['title']:
                    id = i['id']
                    break
                if film.lower() in i['title'].lower():
                    id = i['id']
                    break
            movie = tmdb.Movies(id)
            genres = movie.info(language='it-IT')['genres']
            file[film] = genres
        except IndexError as e:
            print(film + ' non trovato, anno: ' + str(row['Year']))
    
    json_file.close()
    print('Salvataggio...')
    json_object = json.dumps(file)
    with open(path, "w") as outfile:
            outfile.write(json_object)

def get_all_genres():
    genres = tmdb.Genres()
    lst = genres.movie_list(language='it-IT')['genres']
    gens = {}
    for g in lst:
        gens[g['name']] = 0
    return gens

def occ_genres(ita=True, all=False):
    genres = get_all_genres()
    if all:
        json_file = open('Dati_Cinema_Italiani/tables/film_all_genres.json')
    elif ita:
        json_file = open('Dati_Cinema_Italiani/tables/film_ita_genres.json')
    else:
        json_file = open('Dati_Cinema_Italiani/tables/film_other_genres.json')
    file = json.load(json_file)

    for i in file:
        gs = file[i]
        for j in gs:
            if j['name'] not in genres:
                genres[j['name']] = 0
            genres[j['name']] += 1
    return genres

def get_top_actors():
    path = 'Dati_Cinema_Italiani/tables/ita_actors.json'
    json_file = open(path)
    file = json.load(json_file)

    bo = box_offices[box_offices['Naz.'] == 'ITA']

    for index, row in bo.iterrows():
        film = row['Film']

        if film in file:
            continue

        search = tmdb.Search()
        response = search.movie(query=film, language='it-IT')
        try:
            id = search.results[0]['id']
            for i in search.results:
                if film.lower() == i['title']:
                    id = i['id']
                    break
                if film.lower() in i['title'].lower():
                    id = i['id']
                    break
            movie = tmdb.Movies(id)
            credits = movie.credits(language='it-IT')['cast']
            file[film] = credits[:6]
        except IndexError as e:
            print(film + ' non trovato, anno: ' + str(row['Year']))
    
    json_file.close()
    print('Salvataggio...')
    json_object = json.dumps(file)
    with open(path, "w") as outfile:
            outfile.write(json_object)

def get_actors_network(depth=2):
    # json_net = open('Dati_Cinema_Italiani/tables/net_actors.json')
    # file = json.load(json_net)

    act_dict = collections.defaultdict(list)

    path = 'Dati_Cinema_Italiani/tables/ita_actors.json'
    json_file = open(path)
    movie_actor = json.load(json_file)
    
    print('Generazione dati network...')
    for movie in movie_actor:
        actors = movie_actor[movie][:depth]

        for actori in actors:
            if actori['known_for_department'] != 'Acting':
                continue
            actor1 = actori['name']
            for actorj in actors:
                actor2 = actorj['name']

                if actor1 == actor2 or actorj['known_for_department'] != 'Acting':
                    continue

                if actor1 not in act_dict:
                    act_dict[actor1] = [] 
                if actor2 not in act_dict:
                    act_dict[actor2] = []
                act_dict[actor1].append(actor2)
                act_dict[actor2].append(actor1)
    print('Salvataggio...')
    json_object = json.dumps(act_dict)
    with open('Dati_Cinema_Italiani/tables/net_actors.json', "w") as outfile:
            outfile.write(json_object)