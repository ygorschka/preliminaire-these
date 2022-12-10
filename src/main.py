#!/usr/bin/env python3

"""
    Code 1D permettant de resoudre les equations d'Euler
"""

import argparse
from datafile import Data
from finitevolumes import FiniteVolumes
import json
from pathlib import Path
from timeschemes import TimeSchemes

def main():
    # Parser pour recuperer le fichier de cas de test
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', metavar='Test file', type=str,
                        help = 'File describing the test case')
    args = parser.parse_args()
    filename = args.filename

    # Initialisation des classes
    fv = FiniteVolumes(filename)
    ts = TimeSchemes(filename)
    data = Data(filename)

    # Initialisation de certaines variables
    dx = data.get_dx()
    cfl = data.get_cfl()
    dim = data.get_dim()
    which_flux = data.get_which_flux()

    print(f'dx = {cfl}')
    print(f'type of dx = {type(cfl)}')
    print(f'dx = {dim}')
    print(f'type of dx = {type(dim)}')
    print(f'dx = {which_flux}')
    print(f'type of dx = {type(which_flux)}')

    # Permet de créer un dico puis de le sauvegarder
    """l = ['a', 'b', 'c', 'd']
    ll = [1,2,3,4]
    dico = dict()
    for i in range(len(l)):
        dico.update({l[i]: ll[i]})
    with pt.open("w") as tc:
        json.dump(dico, tc, indent=3)"""

    print("\nEnd of file")

if __name__ == "__main__":
    main()
