import unittest
from unittest.suite import TestSuite
from learning import start
from asyncio.runners import run

class Test_me(unittest.TestCase):


    def test_first(self):
        print("my name is first")    
        
    def test_second(self):
        print("her name is second")     
            
if __name__ == "__main__":
    suite=TestSuite()
    test=unittest.TestLoader()
    test.testMethodPrefix = "test_fi"
    suite.addTests(test.loadTestsFromTestCase(Test_me))
    runner=unittest.TextTestRunner()
    runner.run(suite)
    print("No. of test cases present : ", suite.countTestCases())