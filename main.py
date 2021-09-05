import unittest

from case.test_Login import TestLogin

suit = unittest.TestSuite()
suit.addTest(unittest.TestLoader().loadTestsFromTestCase(TestLogin))

runner = unittest.TextTestRunner()
runner.run(suit)