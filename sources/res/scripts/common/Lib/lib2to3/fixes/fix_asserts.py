# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/lib2to3/fixes/fix_asserts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/lib2to3/fixes/fix_asserts.py
from ..fixer_base import BaseFix
from ..fixer_util import Name
NAMES = dict(assert_='assertTrue', assertEquals='assertEqual', assertNotEquals='assertNotEqual', assertAlmostEquals='assertAlmostEqual', assertNotAlmostEquals='assertNotAlmostEqual', assertRegexpMatches='assertRegex', assertRaisesRegexp='assertRaisesRegex', failUnlessEqual='assertEqual', failIfEqual='assertNotEqual', failUnlessAlmostEqual='assertAlmostEqual', failIfAlmostEqual='assertNotAlmostEqual', failUnless='assertTrue', failUnlessRaises='assertRaises', failIf='assertFalse')

class FixAsserts(BaseFix):
    PATTERN = "\n              power< any+ trailer< '.' meth=(%s)> any* >\n              " % ('|').join(map(repr, NAMES))

    def transform(self, node, results):
        name = results['meth'][0]
        name.replace(Name(NAMES[str(name)], prefix=name.prefix))
