import runner
import unittest

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        all_results = {}

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def setUp(self):
        self.Us = runner.Runner("Усэйн", 10)
        self.Andr = runner.Runner("Андрей", 9)
        self.Nik = runner.Runner("Ник", 3)


    @classmethod
    def tearDownClass(cls):
        print("Да")

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены")
    def test_run(self):
        us_andr_nik = runner.Tournament(90, self.Us, self.Andr, self.Nik)
        us_andr_nik.start()
        if self.assertTrue(True):
            print("Андрей")
        else:
            print("Ник")


if __name__ == "__main__":
    unittest.main()