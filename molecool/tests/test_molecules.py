"""
This file contains tests for molecules.
"""

import molecool
import numpy as np

def test_compute_molecular_mass():
    symbols = ["C", "H", "H", "H", "H"]

    calculated_mass = molecool.compute_molecular_mass(symbols)

    expected_mass = 11.0107 + 4*0.00784

    expected_mass = 16.01

    assert np.isclose(calculated_mass, expected_mass, rtol=1e-2)