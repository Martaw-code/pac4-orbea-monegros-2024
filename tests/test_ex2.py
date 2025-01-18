"""
Test module per l'exercici ex2.py usant unittest
"""

import unittest
import pandas as pd
from modules.ex2 import name_surname, elimina_temps_zero, get_ciclista_per_dorsal

class TestEx2(unittest.TestCase):
    """Tests per a les funcions d'ex2.py."""

    def test_name_surname(self):
        """
        Comprova que name_surname canvia la columna 'biker' per noms Faker.
        """
        df = pd.DataFrame({
            "dorsal": [1, 2],
            "biker": ["OldName1", "OldName2"],
            "time": ["00:10:00", "01:10:00"]
        })
        df_anon = name_surname(df)
        # Verifiquem que ja no hi siguin els valors originals
        self.assertFalse(df_anon['biker'].str.contains("OldName").any())

    def test_elimina_temps_zero(self):
        """
        Comprova que elimina_temps_zero elimina files on 'time' == '00:00:00'.
        """
        df = pd.DataFrame({
            "dorsal": [1, 2, 3],
            "biker": ["A", "B", "C"],
            "time": ["00:00:00", "01:00:00", "00:00:00"]
        })
        df_clean = elimina_temps_zero(df)
        self.assertEqual(len(df_clean), 1, "Només hauria de quedar 1 fila amb time != 00:00:00.")

    def test_get_ciclista_per_dorsal(self):
        """
        Comprova la recuperació de ciclista per dorsal.
        """
        df = pd.DataFrame({
            "dorsal": [1000, 2],
            "biker": ["Test1", "Test2"],
            "time": ["01:00:00", "02:00:00"]
        })
        result = get_ciclista_per_dorsal(df, 1000)
        self.assertEqual(len(result), 1, "Hauria de trobar just 1 fila.")
        self.assertEqual(result.iloc[0]["biker"], "Test1")

    def test_get_ciclista_per_dorsal_no_trobat(self):
        """
        Comprova el cas que no troba dorsal.
        """
        df = pd.DataFrame({
            "dorsal": [10, 20],
            "biker": ["T1", "T2"],
            "time": ["01:00:00", "02:00:00"]
        })
        result = get_ciclista_per_dorsal(df, 999)
        self.assertEqual(len(result), 0, "No hauria de trobar cap fila.")


if __name__ == '__main__':
    unittest.main()
