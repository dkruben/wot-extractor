# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/distutils/tests/test_dep_util.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_dep_util.py
import unittest, os, time
from distutils.dep_util import newer, newer_pairwise, newer_group
from distutils.errors import DistutilsFileError
from distutils.tests import support
from test.test_support import run_unittest

class DepUtilTestCase(support.TempdirManager, unittest.TestCase):

    def test_newer(self):
        tmpdir = self.mkdtemp()
        new_file = os.path.join(tmpdir, 'new')
        old_file = os.path.abspath(__file__)
        self.assertRaises(DistutilsFileError, newer, new_file, old_file)
        self.write_file(new_file)
        self.assertTrue(newer(new_file, 'I_dont_exist'))
        self.assertTrue(newer(new_file, old_file))
        self.assertFalse(newer(old_file, new_file))

    def test_newer_pairwise(self):
        tmpdir = self.mkdtemp()
        sources = os.path.join(tmpdir, 'sources')
        targets = os.path.join(tmpdir, 'targets')
        os.mkdir(sources)
        os.mkdir(targets)
        one = os.path.join(sources, 'one')
        two = os.path.join(sources, 'two')
        three = os.path.abspath(__file__)
        four = os.path.join(targets, 'four')
        self.write_file(one)
        self.write_file(two)
        self.write_file(four)
        self.assertEqual(newer_pairwise([one, two], [three, four]), (
         [
          one], [three]))

    def test_newer_group(self):
        tmpdir = self.mkdtemp()
        sources = os.path.join(tmpdir, 'sources')
        os.mkdir(sources)
        one = os.path.join(sources, 'one')
        two = os.path.join(sources, 'two')
        three = os.path.join(sources, 'three')
        old_file = os.path.abspath(__file__)
        self.write_file(one)
        self.write_file(two)
        self.write_file(three)
        self.assertTrue(newer_group([one, two, three], old_file))
        self.assertFalse(newer_group([one, two, old_file], three))
        os.remove(one)
        self.assertRaises(OSError, newer_group, [one, two, old_file], three)
        self.assertFalse(newer_group([one, two, old_file], three, missing='ignore'))
        self.assertTrue(newer_group([one, two, old_file], three, missing='newer'))


def test_suite():
    return unittest.makeSuite(DepUtilTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())
