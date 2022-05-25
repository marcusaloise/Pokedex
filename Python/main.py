#!/bin/python3
import requests
import json
import csv
import pandas as pd


filename = 'Pokemons.csv'
csv_data = [] #[['bulbasaur', 'overgrow, chlorophyll', 'grass, poison']]

f = open(filename, "w+")
f.close()

def getAbilities(pokemondata):
    ability_list = []
    abilities = pokemondata['abilities']       
    for ability in abilities:
        ability_list.append(ability['ability']['name'])


    
    return ability_list


def getType(pokemondata):
    type_list = []
    types = pokemondata['types']       
    for type in types:
        type_list.append(type['type']['name'])

    
    return type_list


def getPokemons(qual_pokemon):
    if not qual_pokemon:
        request = requests.get("https://pokeapi.co/api/v2/pokemon?limit=10&offset=0")

    else:
        
        request = requests.get("https://pokeapi.co/api/v2/pokemon/{}".format(qual_pokemon.lower()))
        if request.status_code == 404:   
            
            raise ValueError("Pokemon não Encontrado")         

    json_response = request.json()

    return json_response

def main():

    qual_pokemon = input ('Informe o nome do pokemon para pesquisa ou aperte enter para obter 10 pokemons.')
    pokemondata = getPokemons(qual_pokemon)
    headerList = ['Name', 'Ability', 'Type']
    with open(filename, 'a', newline="") as file:
        dw = csv.DictWriter(file, delimiter=',', fieldnames=headerList)
        dw.writeheader()
    
    if not qual_pokemon:
        for pokemon in pokemondata['results']:
            request = requests.get(pokemon['url'])
            json_response = request.json()

            ability_list = ' '.join(getAbilities(json_response))
            type_list =  ' '.join(getType(json_response))


            csv_data = [pokemon['name'] + ',' + ability_list + ',' + type_list]

            with open(filename, 'a', newline="") as file:
                csvwriter = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
                csvwriter.writerow(csv_data)
          
    else:
            ability_list = ' '.join(getAbilities(pokemondata))
            type_list =  ' '.join(getType(pokemondata))


            csv_data = [qual_pokemon.lower() + ',' + ability_list + ',' + type_list]

            print(csv_data)

            with open(filename, 'a', newline="") as file:
                csvwriter = csv.writer(file, quoting=csv.QUOTE_NONE, escapechar=' ')
                csvwriter.writerow(csv_data)

    data = pd.read_csv("Pokemons.csv")
    data.sort_values("Ability", axis=0, ascending=[True], inplace=True)


    
    data.to_csv("Pokemons.csv", index=False)



if __name__ == '__main__':
    main()
    