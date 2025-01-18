"""
Test module per l'exercici ex1.py usant unittest
"""

import unittest
import pandas as pd
from modules.ex1 import carrega_conjunt, primers_registres, get_nombre_ciclistes, get_columnes

class TestEx1(unittest.TestCase):
    """Tests per a les funcions d'ex1.py."""

    def test_carrega_conjunt(self):
        """
        Test per comprovar que carrega_conjunt carrega un DataFrame no buit.
        """
        df = carrega_conjunt("data/dataset.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty, "El DataFrame no hauria d'estar buit.")

    def test_primers_registres(self):
        """
        Test per comprovar que primers_registres retorna el nombre de files esperades.
        """
        df = pd.DataFrame({"col1": [1, 2, 3, 4, 5]})
        result = primers_registres(df, 3)
        self.assertEqual(len(result), 3, "Hauria de retornar 3 files.")

    def test_get_nombre_ciclistes(self):
        """
        Test per comprovar que get_nombre_ciclistes retorna el nombre de files del DF.
        """
        df = pd.DataFrame({"col1": [1, 2, 3]})
        result = get_nombre_ciclistes(df)
        self.assertEqual(result, 3)

    def test_get_columnes(self):
        """
        Test per comprovar que get_columnes retorna la llista de columnes.
        """
        df = pd.DataFrame({"a": [1], "b": [2]})
        cols = get_columnes(df)
        self.assertEqual(cols, ["a", "b"])


if __name__ == '__main__': # pragma: no cover
    unittest.main()
