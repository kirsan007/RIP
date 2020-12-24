# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import unittest

testData=[
    [1,4],
    [3,5],
    [6,7]
]

universalTestData=[
    {"a":2,"b":4,"result":6},
    {"a":3,"b":3,"result":6},
    {"a":5,"b":2,"result":7}
]



class Tests(unittest.TestCase):
    def testPlus(self):
        for data in testData:
            self.assertEqual(data[0]+data[1], plus(data[0],data[1]))
    def test(self):
        for data in universalTestData:
            self.assertEqual(data["result"], plus(data["a"], data["b"]))




def plus(a,b):
    return a+b




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    unittest.main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
