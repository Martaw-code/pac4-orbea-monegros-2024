"""
Tests for main.py to ensure 100% coverage of the branching logic.
"""

import unittest
import sys
from unittest.mock import patch
import main

class TestMain(unittest.TestCase):
    """Tests per comprovar la lògica de main.py (cobrir totes les branques)."""

    def test_main_no_args(self):
        """
        Simulem cridar 'python main.py' sense paràmetres -> 'all'.
        """
        testargs = ["main.py"]
        with patch.object(sys, 'argv', testargs):
            main.main()  # Esperem que executi TOT sense errors

    def test_main_ex1(self):
        """
        Simulem 'python main.py --exercise ex1'.
        """
        testargs = ["main.py", "--exercise", "ex1"]
        with patch.object(sys, 'argv', testargs):
            main.main()

    def test_main_ex2(self):
        """
        Simulem 'python main.py --exercise ex2'.
        """
        testargs = ["main.py", "--exercise", "ex2"]
        with patch.object(sys, 'argv', testargs):
            main.main()

    def test_main_ex3(self):
        """
        Simulem 'python main.py --exercise ex3'.
        """
        testargs = ["main.py", "--exercise", "ex3"]
        with patch.object(sys, 'argv', testargs):
            main.main()

    def test_main_ex4(self):
        """
        Simulem 'python main.py --exercise ex4'.
        """
        testargs = ["main.py", "--exercise", "ex4"]
        with patch.object(sys, 'argv', testargs):
            main.main()

    def test_main_ex5(self):
        """
        Simulem 'python main.py --exercise ex5'.
        """
        testargs = ["main.py", "--exercise", "ex5"]
        with patch.object(sys, 'argv', testargs):
            main.main()

    def test_main_unrecognized_exercise(self):
        """
        Simulem 'python main.py --exercise x999' -> branca else
        """
        testargs = ["main.py", "--exercise", "x999"]
        with patch.object(sys, 'argv', testargs):
            main.main()


if __name__ == '__main__':
    unittest.main()
