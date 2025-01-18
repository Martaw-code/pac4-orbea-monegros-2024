"""
Test module for ex5.py using unittest
"""
import unittest
import pandas as pd
from modules.ex5 import get_ucsc_cyclists, get_best_time_ucsc, get_position_and_percentage

class TestEx5(unittest.TestCase):
    """Tests per a les funcions d'ex5.py."""

    def test_get_ucsc_cyclists(self):
        """Comprova el filtre per club_clean == 'UCSC'."""
        df = pd.DataFrame({
            "biker": ["A", "B", "C"],
            "club_clean": ["UCSC", "HUESCA", "UCSC"],
            "time": ["01:00:00", "02:00:00", "03:00:00"],
            "dorsal": [1, 2, 3]
        })
        df_ucsc = get_ucsc_cyclists(df)
        self.assertEqual(len(df_ucsc), 2, "Hauria de trobar 2 ciclistes UCSC.")

    def test_get_best_time_ucsc(self):
        """Comprova que es troba el millor temps dins la UCSC."""
        df = pd.DataFrame({
            "biker": ["X", "Y"],
            "club_clean": ["UCSC", "UCSC"],
            "time": ["01:30:00", "00:50:00"],
            "dorsal": [10, 11]
        })
        best = get_best_time_ucsc(df)
        self.assertEqual(best["dorsal"], 11, "El millor temps hauria de ser dorsal=11 (00:50:00).")

    def test_get_position_and_percentage(self):
        """Comprova la posició i percentatge."""
        df = pd.DataFrame({
            "dorsal": [10, 11, 12],
            "time": ["01:00:00", "00:50:00", "01:30:00"]
        })
        pos, perc = get_position_and_percentage(df, 11)
        self.assertEqual(pos, 1)
        self.assertAlmostEqual(perc, 33.33, places=2)

        pos2, perc2 = get_position_and_percentage(df, 12)
        self.assertEqual(pos2, 3)
        self.assertAlmostEqual(perc2, 100.0, places=2)

    def test_get_position_and_percentage_not_found(self):
        """Comprova el cas de dorsal inexistent."""
        df = pd.DataFrame({
            "dorsal": [10, 20],
            "time": ["01:00:00", "02:00:00"]
        })
        pos, perc = get_position_and_percentage(df, 999)
        self.assertIsNone(pos)
        self.assertIsNone(perc)

    def test_no_ucsc_case(self):
        """
        Comprova el cas on no hi ha ciclistes UCSC (per forçar branques que
        potser tens en la lògica ex5).
        """
        df = pd.DataFrame({
            "biker": ["A", "B"],
            "club_clean": ["HUESCA", "BARCELONA"],
            "time": ["01:00:00", "02:00:00"],
            "dorsal": [1, 2]
        })
        df_ucsc = get_ucsc_cyclists(df)
        self.assertEqual(len(df_ucsc), 0, "No hauria de trobar cap ciclista UCSC.")


if __name__ == '__main__':
    unittest.main()
