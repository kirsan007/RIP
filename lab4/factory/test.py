

import unittest
from factory.program import go, eat

from factory.human import Doctor, Student, Sportsman
name = "Вася"
classes=[Doctor(name), Student(name), Sportsman(name)]

class Tests(unittest.TestCase):
    def testName(self):
        for human in classes:
            with self.subTest(human=human):
                self.assertEqual(human.name, name)

    def test(self):
        for i in range(20):
            human=classes[i%3]
            with self.subTest(i=i, human=human):
                tmpFeed=human.feed
                eat(human)
                self.assertLess(tmpFeed, human.feed)
                tmpPosition=human.position
                tmpFeed = human.feed
                go(human)
                self.assertLess(tmpPosition, human.position)
                self.assertGreater(tmpFeed, human.feed)


if __name__ == '__main__':
    unittest.main()




