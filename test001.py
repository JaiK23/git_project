from logging import Logger
from re import Pattern
from typing import Any
import unittest as ut
from unittest._log import _AssertLogsContext, _LoggingWatcher 
#to write manual tests using unittest
#in older ver. python uses unittest2 (below 3.2 ish)

'''
1) Test cases and Test methods ( with assertion)
'''
class test_cases(ut.TestCase): # call method TestCase to 
    #Must start with "test_"
    def test_with_sum(self):
        assert sum(1,3,4) == 8, "Should be 8"

    def test_with_tup(self):
        assert sum((1,2,5)) == 8, "Should add upto 8"

    def test_with_list(self):
        assert sum([1,3,5]) ==7, "Should be "

    def assertCompare(self): #kind of wrong
        assert self.a == self.b

    def assertLogs(self, logger: str | Logger | None = None, level: int | str | None = None) -> _AssertLogsContext[_LoggingWatcher]:
        return super().assertLogs(logger, level)

    def assertEqual(self):
        self.assertEqual(,)
#To check for String and Regex
    def assertRegex(self, text: AnyStr, expected_regex: AnyStr | Pattern[AnyStr], msg: Any = None) -> None:
        return super().assertRegex(text, expected_regex, msg)
#various methods used to test in Unittest

#We can also skip tests if it interfere with results 
'''
Like this 
@unittest.skip
'''
@ut.skip("Mention why we skipped it")
test_cases.test_with_list()
a = 5
b = 7
@ut.skipIf(a>b,"val is out of bounds")