#!/usr/bin/env python3

class Data:
    """
        Parameters of the problem
    """

    # Recuperer ces informations dans un fichier a terme

    def __init__(self):
        # Longueur du domaine
        self.Lx = 1.0
        # Xo
        self.x0 = 0.0
        # Pas d'espace
        self.dx = 1e-3
        # Coefficient adiabatique
        self.gamma = 1.0

    def get_Lx(self):
        return self.Lx

    def get_dx(self):
        return self.dx

    def get_xo(self):
        return self.xo

    def get_coeff_adiab(self):
        return self.gamma
