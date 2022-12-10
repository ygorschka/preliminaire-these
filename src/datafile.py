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

        # Chemin complet du cas de test
        test_file_path = Path(self.test_path + self.filename)

        # Erreur si le cas de test n'existe pas
        if not test_file_path.exists():
            print("Test case does not exist")
            exit()

        # Liste contenant tous les parametres du cas de test
        Parameters = ['dx','Tf','Lx','x0','dim','cfl','adiab','flux','variable']

        # Recuperer les infos dans le fichier du cas de test
        with test_file_path.open() as tc:
            json_dictionary = tc.read()
            if json_dictionary:
                param_dictionary = json.loads(json_dictionary)

        try :
            # Pas d'espace
            self.dx = param_dictionary['dx']
            # Longueur du domaine
            self.Lx = param_dictionary['Lx']
            # Xo
            self.x0 = param_dictionary['x0']
            # Coefficient adiabatique
            self.gamma = param_dictionary['adiab']
            # Tf
            self.Tf = param_dictionary['Tf']
            # Dimension du probleme
            self.dim = param_dictionary['dim']
            # CFL
            self.cfl = param_dictionary['cfl']
            # Choix du flux - Roe
            self.which_flux = param_dictionary['flux']
            # Choix des variables - conserved ou primitives
            self.variable = param_dictionary['variable']
        except KeyError:
            print("Error test file")
            exit()

    def get_which_flux(self):
        return self.which_flux

    def get_variable(self):
        return self.variable

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

    def get_tf(self):
        return self.Tf
