#!/usr/bin/env python3

"""
    Code 1D permettant de resoudre les equations d'Euler
"""

import argparse
from datafile import Data
from finitevolumes import FiniteVolumes
import json
from timeschemes import TimeSchemes

def main():
    # Initialisation des classes
    fv = FiniteVolumes()
    ts = TimeSchemes()
    data = Data()

    # Initialisation de certaines variables
    test_path = data.get_test_path()

    parser = argparse.ArgumentParser()
    # Test pour les parsers
    parser.add_argument('filename', metavar='Test file', type=str,
                        help = 'File describing the test case')
    args = parser.parse_args()
    filename = args.filename

    try:
        file = open(test_path + filename, 'r')
        nb = float(file.readline())
        file.close()
    except FileNotFoundError:
        print("Test case file not found")
        exit(1)

    print(f"nb = {nb}")

    print("\nEnd of file")

if __name__ == "__main__":
    main()
