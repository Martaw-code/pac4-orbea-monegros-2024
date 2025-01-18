"""
Test module per l'exercici ex3.py usant unittest
"""

import unittest
import os
import pandas as pd
from modules.ex3 import minutes_002040, crea_time_grouped, groupby_time_grouped, plot_histograma

class TestEx3(unittest.TestCase):
    """Tests per a les funcions d'ex3.py."""

    def test_minutes_002040(self):
        """Comprova l'agrupació en 00, 20 o 40 segons el minut."""
        self.assertEqual(minutes_002040("06:19:59"), "06:00")
        self.assertEqual(minutes_002040("06:20:00"), "06:20")
        self.assertEqual(minutes_002040("06:39:59"), "06:20")
        self.assertEqual(minutes_002040("06:40:00"), "06:40")
        self.assertEqual(minutes_002040("06:59:59"), "06:40")

    def test_crea_time_grouped(self):
        """Comprova que la funció afegeix la columna 'time_grouped' correctament."""
        df = pd.DataFrame({
            "dorsal": [1, 2],
            "time": ["01:05:00", "01:35:00"]
        })
        df_new = crea_time_grouped(df)
        self.assertIn("time_grouped", df_new.columns)
        self.assertEqual(df_new.loc[0, "time_grouped"], "01:00")
        self.assertEqual(df_new.loc[1, "time_grouped"], "01:20")

    def test_groupby_time_grouped(self):
        """Comprova el groupby time_grouped."""
        df = pd.DataFrame({
            "time_grouped": ["00:00", "00:00", "00:20", "00:40", "00:40"]
        })
        grouped_df = groupby_time_grouped(df)
        # Esperem: 3 files (00:00 -> 2, 00:20 ->1, 00:40->2), total 5
        self.assertEqual(len(grouped_df), 3)
        self.assertEqual(grouped_df["count"].sum(), 5)

    def test_plot_histograma(self):
        """Comprova que la funció plot_histograma genera un fitxer PNG."""
        df = pd.DataFrame({
            "time_grouped": ["00:00", "00:00", "00:20"],
            "count": [2, 2, 1]
        })
        output_path = "img/test_histograma.png"

        plot_histograma(df, output_path)
        self.assertTrue(
            os.path.exists(output_path),
            "S'hauria d'haver creat el fitxer de l'histograma.")


if __name__ == '__main__': # pragma: no cover
    unittest.main()
