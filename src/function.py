#!/usr/bin/env python3

from datafile import Data

class Function:
    """
        Various functions
    """

    def __init__(self):
        # Initialisation des classes
        data = Data()

        # Initialisation de certaines variables
        self.coeff_adiab = data.get_coeff_adiab()


    # Calcul l'energie interne
    def internal_energy(self,
                        p: float,
                        rho: float):

        internal_e = p/((self.coeff_adiab - 1.0)*rho)

        return internal_e

    # Calcul de l'energie totale
    def total_energy(self,
                     e: float,
                     rho: float,
                     u: float):

        total_e = 0.5*rho*u*u + rho*e

        return total_e

    # Calcul l'enthalpie  totale
    def total_enthalpy(self,
                       E: float,
                       p: float,
                       rho: float):

        H = (E + p)/rho

        return H
