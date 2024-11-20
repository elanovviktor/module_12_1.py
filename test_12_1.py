import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunerTest(unittest.TestCase):
    def test_walk(self):
        vik_runner = Runner('Walk')
        for i in range(10):
            vik_runner.walk()
        self.assertEqual(vik_runner.distance, 50)

    def test_run(self):
        vik_runner = Runner('Run')
        for i in range(10):
            vik_runner.run()
        self.assertEqual(vik_runner.distance, 100)

    def test_challenge(self):
        vik_runner = Runner('Walk_1')
        nata_runner = Runner('Run_1')
        for i in range(10):
            vik_runner.walk()
            nata_runner.run()
        self.assertNotEqual(vik_runner.distance, nata_runner.distance)

if __name__ == '__main__':
    unittest.main()