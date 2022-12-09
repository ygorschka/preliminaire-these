#!/usr/bin/env python3

from datafile import Data
from function import Function
import math
import numpy as np

class FiniteVolumes:
    """
        Finite volumes schemes
    """

    def __init__(self,filename):
        # Initialisation des classes
        self.data = Data(filename)
        self.fct = Function(filename)

        # Initialisation de certaines variables
        self.coeff_adiab = self.data.get_coeff_adiab()
        self.dim = self.data.get_dim()

    # Calcul les quantites moyennes de Roe
    def Roe_average(self,
                    W_l: np.ndarray,
                    W_r: np.ndarray):

        # Recuperation des variables
        if self.dim == 1:
            u_l = W_l[0]; rho_l = W_l[1]; p_l = W_l[2]
            u_r = W_r[0]; rho_r = W_r[1]; p_r = W_r[2]
        elif self.dim == 2:
            u_l = W_l[0]; v_l = W_l[1]; rho_l = W_l[2]; p_l = W_l[3]
            u_r = W_r[0]; v_r = W_r[1]; rho_r = W_r[2]; p_r = W_r[3]
        else:
            print("Error dimension >2")
            exit()

        # Calcul de l'energie
        internal_el = self.fct.internal_energy(p_l, rho_l)
        internal_er = self.fct.internal_energy(phr, rho_r)
        E_l = self.fct.total_energy(internal_el, rho_l, u_l)
        E_r = self.fct.total_energy(internal_er, rho_r, u_r)

        # Calcul de l'enthalpie
        H_l = self.fct.total_enthalpy(E_l, p_l, rho_l)
        H_r = self.fct.total_enthalpy(E_r, p_r, rho_r)

        # Calcul des valeurs moyennes de Roe
        denominateur_tilde = math.sqrt(rho_l)+math.sqrt(rho_r)
        sqrt_rhol = math.sqrt(rho_l)
        sqrt_rhor = math.sqrt(rho_r)

        rho_tilde = math.sqrt(rho_l*rho_r)

        u_tilde = (sqrt_rhol*u_l + sqrt_rhor*u_r)/denominateur_tilde
        if self.dim == 2:
            v_tilde = (sqrt_rhol*v_l + sqrt_rhor*v_r)/denominateur_tilde

        H_tilde = (sqrt_rhol*H_l + sqrt_rhor*H_r)/denominateur_tilde

        if self.dim == 1:
            v_tilde_square = fct.velocity_square(u_tilde)
        elif self.dim == 2:
            v_tilde_square = fct.velocity_square(u_tilde, v_tilde)
        else:
            print("Error dimension >2")
            exit()
        a_tilde = math.sqrt((self.coeff_adiab-1)*(H_tilde-0.5*v_tilde_square))

        if self.dim == 1:
            average = np.array([rho_tilde, u_tilde, H_tilde, a_tilde])
        elif self.dim == 2:
            average = np.array([rho_tilde, u_tilde, v_tilde, H_tilde, a_tilde])

        return average

    # Calcul des valeurs propres
    def Roe_eigenvalues(self,
                        u: float,
                        a: float):

        eigenvalues = np.zeros(2+self.dim)
        eigenvalues[0] = u-a
        eigenvalues[1] = u
        if dim == 2:
            eigenvalues[2] = u
        eigenvalues[-1] = u+a

        return eigenvalues

    # Calcul des vecteurs propres
    def Roe_eigenvectors(self,
                         u: float,
                         a: float,
                         H: float,
                         v: float = 0.0):

        size = self.dim + 2
        v_square = self.fct.velocity_square(u,v)

        K1 = np.zeros(size) ;K2 = np.zeros(size); K3 = np.zeros(size)
        if self.dim == 1:
            K1[0] = 1; K1[1] = u-a; K1[2] = H-u*a
            K2[0] = 1; K2[1] = u;   K2[2] = 0.5*v_square
            K3[0] = 1; K3[1] = u+a; K3[2] = H+u*a

            eigenvectors = (K1, K2, K3)
        elif self.dim == 2:
            K4 = np.zeros(size)
            K1[0] = 1; K1[1] = u-a; K1[2] = v; K1[3] = H-u*a
            K2[0] = 1; K2[1] = u;   K2[2] = v; K2[3] = 0.5*v_square
            K3[0] = 0; K3[1] = 0;   K3[2] = 1; K3[3] = v
            K4[0] = 1; K4[1] = u+a; K4[2] = v; K4[3] = H+u*a

            eigenvectors(K1, K2, K3, K4)
        else:
            print("Error dimension >2")
            exit()

        return eigenvectors

    # Calcul des vitesses d'onde
    def wave_strength(self,
                      W_l: np.ndarray,
                      W_r: np.ndarray):

        # Taille des tableaux
        size = self.dim + 2

        # Recuperation des variables
        if self.dim == 1:
            u_l = W_l[0]; rho_l = W_l[1]; p_l = W_l[2]
            u_r = W_r[0]; rho_r = W_r[1]; p_r = W_r[2]
        elif self.dim == 2:
            u_l = W_l[0]; v_l = W_l[1]; rho_l = W_l[2]; p_l = W_l[3]
            u_r = W_r[0]; v_r = W_r[1]; rho_r = W_r[2]; p_r = W_r[3]
        else:
            print("Error dimension >2")
            exit()

        # Calcul delta
        delta_p = p_r - p_l
        delta_u = u_r - u_l
        delta_rho = rho_r - rho_l
        if self.dim == 2:
            delta_v = v_r - v_l

        # Recupertation valeurs moyennes
        average = self.Roe_average(W_l,W_r)
        rho_tilde = average[0]
        a_tilde = average[-1]

        # Calcul des vitesses d'onde
        wave = np.zeros(size)
        square_a_tilde = pow(a_tilde,2)
        factor = 1/(2*square_a_tilde)

        wave[0] = factor*(delta_p - rho_tilde*a_tilde*delta_u)
        wave[1] = delta_rho - delta_p/square_a_tilde
        wave[-1] = factor*(delta_p + rho_tilde*a_tilde*delta_u)

        if self.dim == 2:
            wave[2] = rho_tilde*delta_v

        return wave

    # Calcul F(U) pour U donne - on travaille avec les variables primitives
    def FU(self,
           W: np.ndarray):

        if self.dim == 2:
            print("Cas 2D pas encore implemente")
            exit()

        # Initialisation du vecteur
        size = np.size(W)
        FU = np.zeros(size)

        # Recuperation des donnees
        rho = W[0];
        u = W[1];
        p = W[-1]
        velocity_square = self.fct.velocity_square(u)
        internal_e = self.fct.internal_energy(p, rho)
        total_e = self.fct.total_energy(internal_e, rho, u)

        # Construction de la solution
        FU[0] = rho*u
        FU[1] = rho*velocity_square + p
        FU[-1] = total_e

    # Calcul flux de Roe
    def Roe(self):
        None
