"""
Test module per l'exercici ex4.py usant unittest
"""

import unittest
import pandas as pd
from modules.ex4 import clean_club, afegir_columna_clean_club, groupby_club_clean

class TestEx4(unittest.TestCase):
    """Tests per a les funcions d'ex4.py."""

    def test_clean_club(self):
        """Comprova la neteja de noms de clubs."""
        self.assertEqual(clean_club("C.C. HUESCA"), "HUESCA")
        self.assertEqual(clean_club("PEÑA CICLISTA GIRONA"), "GIRONA")
        self.assertEqual(clean_club("  CLUB CICLISTA BARCELONA  TT"), "BARCELONA")
        self.assertEqual(clean_club("A.C. LLEIDA C.C."), "LLEIDA")

    def test_afegir_columna_clean_club(self):
        """Comprova que s'afegeix la columna 'club_clean'."""
        df = pd.DataFrame({
            "club": ["C.C. HUESCA", "PEÑA CICLISTA GIRONA", "INDP"]
        })
        df_new = afegir_columna_clean_club(df)
        self.assertIn("club_clean", df_new.columns)
        self.assertEqual(df_new.loc[0, "club_clean"], "HUESCA")
        self.assertEqual(df_new.loc[1, "club_clean"], "GIRONA")
        self.assertEqual(df_new.loc[2, "club_clean"], "INDP")

    def test_groupby_club_clean(self):
        """Comprova l'agrupació per 'club_clean'."""
        df = pd.DataFrame({
            "club_clean": ["HUESCA", "HUESCA", "SARIÑENA", "GIRONA", "SARIÑENA", "SARIÑENA"]
        })
        grouped_df = groupby_club_clean(df)
        # HUESCA=2, SARIÑENA=3, GIRONA=1 => total 6
        self.assertEqual(len(grouped_df), 3)
        self.assertEqual(grouped_df["count"].sum(), 6)
        top_club = grouped_df.iloc[0]["club_clean"]
        top_count = grouped_df.iloc[0]["count"]
        self.assertEqual(top_club, "SARIÑENA")
        self.assertEqual(top_count, 3)


if __name__ == '__main__': # pragma: no cover
    unittest.main()
