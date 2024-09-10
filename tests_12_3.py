import runner
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_walk(self):
        ocr = runner.Runner("Олег")
        for _ in range(10):
            ocr.walk()
        self.assertEqual(ocr.distance, 50)

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_run(self):
        ocr = runner.Runner("Олег")
        for _ in range(10):
            ocr.run()
        self.assertEqual(ocr.distance, 100)

    @unittest.skipIf(is_frozen, "Запускаем тест")
    def test_challenge(self):
        Elena = runner.Runner("Елена")
        Tat = runner.Runner("Татьяна")
        for _ in range(10):
            Elena.walk()
            Tat.run()
        self.assertNotEqual(Elena.distance, Tat.distance)

if __name__ == "__main":
    unittest.main