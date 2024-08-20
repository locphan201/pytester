import unittest
from colorama import Fore, Style, init

init(autoreset=True)

class ColoredTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return ColoredTestResult(self.stream, self.descriptions, self.verbosity)

class ColoredTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        self.stream.write(f'{Fore.GREEN}PASS - {str(test).split(" ")[1]} {str(test).split(" ")[0]}{Style.RESET_ALL}\n')
        self.stream.flush()
    
    def addFailure(self, test, err):
        self.stream.write(f'{Fore.RED}FAIL - {str(test).split(" ")[1]} {str(test).split(" ")[0]}{Style.RESET_ALL}\n')
        self.stream.flush()
    
    def addError(self, test, err):
        self.addFailure(test, err)
        
    def stopTest(self, test):
        super().stopTest(test)
        
    def printErrors(self):
        if self.failures:
            self.stream.write(f'{Fore.RED}Failures:{Style.RESET_ALL}\n')
            super().printErrors()
        if self.errors:
            self.stream.write(f'{Fore.RED}Errors:{Style.RESET_ALL}\n')
            super().printErrors()


################################################
#                  TEST CASES                  #
################################################

from examples import *

class TestExampleFunctions(unittest.TestCase):
    def test_example_text(self):
        self.assertEqual(example_text(), 'example')
        
    def test_example_numbers(self):
        self.assertEqual(example_number(), 0)

if __name__ == "__main__":
    result = unittest.main(testRunner=ColoredTestRunner())