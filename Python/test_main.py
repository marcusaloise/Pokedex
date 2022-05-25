#!/bin/python3
from textwrap import dedent
import unittest

import json

from requests import get

from main import getAbilities
from main import getType
from main import getPokemons
from main import main

data = json.load(open('pikachu.json'))

class TestPokedex(unittest.TestCase):
    # Teste do getPokemon
    def test_getPokemon(self):
        self.assertRaises(ValueError, getPokemons, "marcus")
        teste_getPokemon = getPokemons("Pikachu")
        if "abilities" in teste_getPokemon:
            ability_key = True
        else:
            ability_key = False

        if "types" in teste_getPokemon:
            type_key = True
        else:
            type_key = False

        print()

        self.assertEqual(ability_key, True, "A chave ability não existe")
        self.assertEqual(type_key, True, "A chave type não existe")

    # Teste do GetType
    def test_getType(self):
        get_type = getType(data)
        self.assertIsInstance(get_type, list, "A função getType não retornou uma lista")
          
    # Teste do GetAbilities
    def test_getAbilities(self):
        get_abilities = getAbilities(data)
        self.assertIsInstance(get_abilities, list, "A função getType não retornou uma lista")
        

    # Validando csv
    #def test_csv(self):
    #    main()
