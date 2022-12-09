#!/usr/bin/env python3

class Data:
    """
        Parameters of the problem
    """

    # Recuperer ces informations dans un fichier a terme

    def __init__(self):
        # Path pour les cas de test
        self.test_path = "/mnt/c/Users/ygors/Documents/Thèse/preliminaire/test_case/"
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
