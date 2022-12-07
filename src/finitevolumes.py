#!/usr/bin/env python3

from datafile import Data
from function import Function
import math
import numpy as np

class FiniteVolumes:
    """
        Finite volumes schemes
    """

    def __init__(self):
        # Initialisation des classes
        data = Data()
        fct = Function()

        # Initialisation de certaines variables
        self.coeff_adiab = data.get_coeff_adiab()

    # Calcul les quantites moyennes de Roe
    def Roe_average(self,
                    W_l: np.array,
                    W_r: np.array):

        # Recuperation des variables
        u_l = W_l[0], rho_l = W_l[1], p_l = W_l[2]
        u_r = W_r[0], rho_r = W_r[1], p_r = W_r[2]

        # Calcul de l'energie
        internal_e_l = fct.internal_energy(p_l, rho_l)
        internal_e_r = fct.internal_energy(phr, rho_r)
        E_l = fct.total_energy(internal_e_l, rho_l, u_l)
        E_r = fct.total_energy(internal_e_r, rho_r, u_r)

        # Calcul de l'enthalpie
        H_l = fct.total_enthalpy(E_l, p_l, rho_l)
        H_r = fct.total_enthalpy(E_r, p_r, rho_r)

        # Calcul des valeurs moyennes de Roe
        u_tilde =

    # Calcul des valeurs propres
    def Roe_eigenvalues(self):
        None

    # Calcul des vecteurs propres
    def Rie_eigenvectors(self):
        None

    # Calcul des vitesses d'ondes
    def wave_strength(sefl):
        None

    def Roe(self):
        None
