import unittest

# Importem les classes de test de cadascun dels fitxers
from tests.test_ex1 import TestEx1
from tests.test_ex2 import TestEx2
from tests.test_ex3 import TestEx3
from tests.test_ex4 import TestEx4
from tests.test_ex5 import TestEx5
from tests.test_main import TestMain

def suite() -> unittest.TestSuite:
    """
    Crea i retorna una TestSuite que agrupi tots els tests
    definits a les classes TestEx1, TestEx2, ..., TestMain.
    """
    # Creem una TestSuite buida
    test_suite = unittest.TestSuite()

    # Afegim cadascuna de les nostres classes de test
    test_suite.addTest(unittest.makeSuite(TestEx1))
    test_suite.addTest(unittest.makeSuite(TestEx2))
    test_suite.addTest(unittest.makeSuite(TestEx3))
    test_suite.addTest(unittest.makeSuite(TestEx4))
    test_suite.addTest(unittest.makeSuite(TestEx5))
    test_suite.addTest(unittest.makeSuite(TestMain))

    return test_suite


if __name__ == "__main__":
    # Executem la suite amb un TextTestRunner
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())

