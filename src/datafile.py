#!/usr/bin/env python3

class Parameters:
    """
        Parameters of the problem
    """

    def __init__(self):
        # Longueur du domaine
        self.Lx = 1.0

        # Pas d'espace
        self.dx = 1e-3

    def get_Lx(self):
        return self.Lx

    def get_dx(self):
        return self.dx
