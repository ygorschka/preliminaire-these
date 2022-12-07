#!/usr/bin/env python3

from datafile import Data
import numpy as np

class FiniteVolumes:
    """
        Finite volumes schemes
    """

    def __init__(self):
        data = Data()
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

    # Calcul les quantites moyennes de Roe
    def Roe_average(self,
                    W_l: np.array,
                    W_r: np.array):
        # Recuperations des variables
        u_l = W_l[0], rho_l = W_l[1], p_l = W_l[2]
        u_r = W_r[0], rho_r = W_r[1], p_r = W_r[2]

        # Calculs de l'energie
        internal_e_l = self.internal_energy(p_l, rho_l)
        internal_e_r = self.internal_energy(phr, rho_r)


    def Roe(self):
        None
