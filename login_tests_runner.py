import unittest
import login_tests
import xmlrunner


webTestSuite = unittest.TestSuite()
webTestSuite.addTest(unittest.makeSuite(login_tests.LoginTests))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(webTestSuite)