# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/distutils/tests/test_bdist.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/distutils/tests/test_bdist.py
import os, unittest
from test.test_support import run_unittest
from distutils.command.bdist import bdist
from distutils.tests import support

class BuildTestCase(support.TempdirManager, unittest.TestCase):

    def test_formats(self):
        dist = self.create_dist()[1]
        cmd = bdist(dist)
        cmd.formats = ['msi']
        cmd.ensure_finalized()
        self.assertEqual(cmd.formats, ['msi'])
        formats = [
         'bztar', 'gztar', 'msi', 'rpm', 'tar', 
         'wininst', 
         'zip', 'ztar']
        found = sorted(cmd.format_command)
        self.assertEqual(found, formats)

    def test_skip_build(self):
        dist = self.create_dist()[1]
        cmd = bdist(dist)
        cmd.skip_build = 1
        cmd.ensure_finalized()
        dist.command_obj['bdist'] = cmd
        names = [
         'bdist_dumb', 'bdist_wininst']
        if os.name == 'nt':
            names.append('bdist_msi')
        for name in names:
            subcmd = cmd.get_finalized_command(name)
            self.assertTrue(subcmd.skip_build, '%s should take --skip-build from bdist' % name)


def test_suite():
    return unittest.makeSuite(BuildTestCase)


if __name__ == '__main__':
    run_unittest(test_suite())
