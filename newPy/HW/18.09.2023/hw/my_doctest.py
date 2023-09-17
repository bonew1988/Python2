import doctest
from my_task import Rectangle


def load_tests(loader, tests, ignore):
    tests.addTests(doctest.DocTestSuite(Rectangle))
    return tests


if __name__ == '__main__':
    doctest.testmod(verbose=True)
