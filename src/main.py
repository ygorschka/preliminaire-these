#!/usr/bin/env python3

"""
    Code 1D permettant de resoudre les equations d'Euler
"""

from finitevolumes import FiniteVolumes
from datafile import Data
from timeschemes import TimeSchemes


def main():
    # Initialisation des classes
    fv = FiniteVolumes()
    ts = TimeSchemes()
    data = Data()

    print("\nEnd of file")

if __name__ == "__main__":
    main()
