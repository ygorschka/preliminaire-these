#!/usr/bin/env python3

import json
from pathlib import Path

class Data:
    """
        Parameters of the problem
    """

    # Recuperer ces informations dans un fichier a terme

    def __init__(self, filename: str):
        # Path pour les cas de test
        self.test_path = "/mnt/c/Users/ygors/Documents/Thèse/preliminaire/test_case/"
        # Nom du cas de test
        self.filename = filename
        # Longueur du domaine
        self.Lx = 1.0
        # Xo
        self.x0 = 0.0
        # Pas d'espace
        self.dx = 1e-3
        # Coefficient adiabatique
        self.gamma = 1.0
        # Dimension du probleme
        self.dim = 1
        # CFL
        self.cfl = 0.9

        # Chemin complet du cas de test
        test_file_path = Path(self.test_path + filename)

        # Erreur si le cas de test n'existe pas
        if not test_file_path.exists():
            print("Test case does not exist")
            exit()

        # Liste contenant tous les parametres du cas de test
        Parameters = ['a','b','c','d']

        # Recuperer les infos dans le fichier du cas de test
        with test_file_path.open() as tc:
            json_dictionary = tc.read()
            if json_dictionary:
                test_dictionary = json.loads(json_dictionary)

        for e in Parameters:
            try :
                param = test_dictionary[e]
            except KeyError:
                print("Error in test file")
                exit()

    def get_Lx(self):
        return self.Lx

    def get_dx(self):
        return self.dx

    def get_xo(self):
        return self.xo

    def get_coeff_adiab(self):
        return self.gamma

    def get_dim(self):
        return self.dim

    def get_cfl(self):
        return self.cfl

    def get_test_path(self):
        return self.test_path
