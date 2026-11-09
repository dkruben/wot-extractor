# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/unittest/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/unittest/__init__.py
__all__ = [
 'TestResult', 'TestCase', 'TestSuite', 
 'TextTestRunner', 'TestLoader', 
 'FunctionTestCase', 'main', 
 'defaultTestLoader', 'SkipTest', 'skip', 'skipIf', 
 'skipUnless', 
 'expectedFailure', 'TextTestResult', 'installHandler', 
 'registerResult', 
 'removeResult', 'removeHandler']
__all__.extend(['getTestCaseNames', 'makeSuite', 'findTestCases'])
__unittest = True
from .result import TestResult
from .case import TestCase, FunctionTestCase, SkipTest, skip, skipIf, skipUnless, expectedFailure
from .suite import BaseTestSuite, TestSuite
from .loader import TestLoader, defaultTestLoader, makeSuite, getTestCaseNames, findTestCases
from .main import TestProgram, main
from .runner import TextTestRunner, TextTestResult
from .signals import installHandler, registerResult, removeResult, removeHandler
_TextTestResult = TextTestResult
