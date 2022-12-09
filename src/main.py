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
    # Initialisation des classes
    fv = FiniteVolumes()
    ts = TimeSchemes()
    data = Data()

    # Initialisation de certaines variables
    test_path = data.get_test_path()

    # Parser pour recuperer le fichier de cas de test
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', metavar='Test file', type=str,
                        help = 'File describing the test case')
    args = parser.parse_args()
    filename = args.filename

    test_file_path = Path(test_path + filename)

    if not test_file_path.exists():
        print("Test case does not exist")
        exit()

    # Permet de créer un dico puis de le sauvegarder
    """l = ['a', 'b', 'c', 'd']
    ll = [1,2,3,4]
    dico = dict()
    for i in range(len(l)):
        dico.update({l[i]: ll[i]})

    with pt.open("w") as tc:
        json.dump(dico, tc, indent=3)"""

    # Test récupérer les infos des fichiers de cas de test
    with test_file_path.open() as tc:
        json_dictionary = tc.read()
        if json_dictionary:
            test_dictionary = json.loads(json_dictionary)

    print(f"test_dictionary = {test_dictionary['av']}")

    # Erreur pour l'entree d'un dico : KeyError

    print("\nEnd of file")

if __name__ == "__main__":
    main()
