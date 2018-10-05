import unittest
import choose_city_tests


webTestSuite = unittest.TestSuite()
webTestSuite.addTest(unittest.makeSuite(choose_city_tests.ChooseCityTests))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(webTestSuite)