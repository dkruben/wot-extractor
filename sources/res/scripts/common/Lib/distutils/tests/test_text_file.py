# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/distutils/tests/test_text_file.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_text_file.py
import os, unittest
from distutils.text_file import TextFile
from distutils.tests import support
from test.test_support import run_unittest
TEST_DATA = '# test file\n\nline 3 \\\n# intervening comment\n  continues on next line\n'

class TextFileTestCase(support.TempdirManager, unittest.TestCase):

    def test_class(self):
        result1 = [
         '# test file\n', '\n', 'line 3 \\\n', 
         '# intervening comment\n', 
         '  continues on next line\n']
        result2 = [
         '\n',
         'line 3 \\\n',
         '  continues on next line\n']
        result3 = [
         '# test file\n',
         'line 3 \\\n',
         '# intervening comment\n',
         '  continues on next line\n']
        result4 = [
         'line 3 \\',
         '  continues on next line']
        result5 = [
         'line 3   continues on next line']
        result6 = [
         'line 3 continues on next line']

        def test_input(count, description, file, expected_result):
            result = file.readlines()
            self.assertEqual(result, expected_result)

        tmpdir = self.mkdtemp()
        filename = os.path.join(tmpdir, 'test.txt')
        out_file = open(filename, 'w')
        try:
            out_file.write(TEST_DATA)
        finally:
            out_file.close()

        in_file = TextFile(filename, strip_comments=0, skip_blanks=0, lstrip_ws=0, rstrip_ws=0)
        try:
            test_input(1, 'no processing', in_file, result1)
        finally:
            in_file.close()

        in_file = TextFile(filename, strip_comments=1, skip_blanks=0, lstrip_ws=0, rstrip_ws=0)
        try:
            test_input(2, 'strip comments', in_file, result2)
        finally:
            in_file.close()

        in_file = TextFile(filename, strip_comments=0, skip_blanks=1, lstrip_ws=0, rstrip_ws=0)
        try:
            test_input(3, 'strip blanks', in_file, result3)
        finally:
            in_file.close()

        in_file = TextFile(filename)
        try:
            test_input(4, 'default processing', in_file, result4)
        finally:
            in_file.close()

        in_file = TextFile(filename, strip_comments=1, skip_blanks=1, join_lines=1, rstrip_ws=1)
        try:
            test_input(5, 'join lines without collapsing', in_file, result5)
        finally:
            in_file.close()

        in_file = TextFile(filename, strip_comments=1, skip_blanks=1, join_lines=1, rstrip_ws=1, collapse_join=1)
        try:
            test_input(6, 'join lines with collapsing', in_file, result6)
        finally:
            in_file.close()


def test_suite():
    return unittest.makeSuite(TextFileTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())
