from pyvis.network import Network
import networkx as nx
import pandas as pd
import json
from tmdb_api import *
from utility import *

def show_ita_actors_net(min_weight=0, depth=2, buttons=False):
    get_actors_network(depth=depth)

    json_file = open('Dati_Cinema_Italiani/tables/net_actors.json')
    file = json.load(json_file)

    print('Generazione network...')
    actors_net = Network(height="700px", width="100%", bgcolor="#222222", font_color="white", filter_menu=True)
    actors_net.barnes_hut()
    # actors_net.repulsion()

    for actor in file:
        actors_net.add_node(actor, label=actor, title=actor)

    for nodei in actors_net.nodes:
        adj = file[nodei['title']]
        for i in adj:
            weight = 0
            for j in adj:
                if i == j:
                    weight += 1
            actors_net.add_edge(nodei['title'], i, value=weight, title=nodei['title'] + ' - ' + i + ', ' + str(weight))

    neighbor_map = actors_net.get_adj_list()

    for node in actors_net.nodes:
        node["title"] += " Neighbors:\n" + "\n".join(neighbor_map[node["id"]])
        # node["value"] = len(neighbor_map[node["id"]])
    for edge in actors_net.edges:
        if (edge['value'] < min_weight):
            edge['hidden'] = True

    print('Network creata')
    print('numero nodi: ' + str(len(actors_net.nodes)))
    print('numero archi: ' + str(len(actors_net.edges)))

    if buttons:
        actors_net.show_buttons()
    actors_net.show("actors_net.html")

show_ita_actors_net(min_weight=0, depth=3, buttons=True)