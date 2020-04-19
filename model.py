from SPARQLWrapper import SPARQLWrapper
import json_lines


# get player info from json file
def get_player_info():
    dataset = list()
    with open('./data/player.json') as f:
        for each in json_lines.reader(f):
            dataset.append(each)
    return dataset


# connect to the fuseki-server
def initial_connection():
    sparql = SPARQLWrapper('http:localhost:3030/test/query')
    return sparql
