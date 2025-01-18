"""
Test module per l'exercici ex1.py usant unittest
"""

import unittest
import pandas as pd
from modules.ex1 import load_dataset, show_head, get_num_cyclists, get_columns

class TestEx1(unittest.TestCase):
    """Tests per a les funcions d'ex1.py."""

    def test_load_dataset(self):
        """
        Test per comprovar que load_dataset carrega un DataFrame no buit.
        """
        df = load_dataset("../data/dataset.csv")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertFalse(df.empty, "El DataFrame no hauria d'estar buit.")

    def test_show_head(self):
        """
        Test per comprovar que show_head retorna el nombre de files esperades.
        """
        df = pd.DataFrame({"col1": [1, 2, 3, 4, 5]})
        result = show_head(df, 3)
        self.assertEqual(len(result), 3, "Hauria de retornar 3 files.")

    def test_get_num_cyclists(self):
        """
        Test per comprovar que get_num_cyclists retorna el nombre de files del DF.
        """
        df = pd.DataFrame({"col1": [1, 2, 3]})
        result = get_num_cyclists(df)
        self.assertEqual(result, 3)

    def test_get_columns(self):
        """
        Test per comprovar que get_columns retorna la llista de columnes.
        """
        df = pd.DataFrame({"a": [1], "b": [2]})
        cols = get_columns(df)
        self.assertEqual(cols, ["a", "b"])


if __name__ == '__main__':
    unittest.main()
