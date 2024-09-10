import unittest
import tests_12_3
import tests_12_3_1

run_tour = unittest.TestSuite()
run_tour.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
run_tour.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_1.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(run_tour)
