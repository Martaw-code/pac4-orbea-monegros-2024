"""
Suite de testos que agrupa tots els tests definits
"""
import unittest


from tests.test_ex1 import TestEx1
from tests.test_ex2 import TestEx2
from tests.test_ex3 import TestEx3
from tests.test_ex4 import TestEx4
from tests.test_ex5 import TestEx5
from tests.test_main import TestMain

def suite() -> unittest.TestSuite:
    """
    Crea i retorna una TestSuite que agrupa tots els tests
    definits a les classes TestEx1, TestEx2, ..., TestMain,
    sense fer servir unittest.makeSuite().
    """
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    test_suite.addTests([
        loader.loadTestsFromTestCase(TestEx1),
        loader.loadTestsFromTestCase(TestEx2),
        loader.loadTestsFromTestCase(TestEx3),
        loader.loadTestsFromTestCase(TestEx4),
        loader.loadTestsFromTestCase(TestEx5),
        loader.loadTestsFromTestCase(TestMain),
    ])
    return test_suite

if __name__ == "__main__": # pragma: no cover
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite())
