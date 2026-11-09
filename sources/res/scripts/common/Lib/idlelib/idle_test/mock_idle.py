# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/Lib/idlelib/idle_test/mock_idle.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/Lib/idlelib/idle_test/mock_idle.py
from idlelib.idle_test.mock_tk import Text

class Func(object):

    def __init__(self, result=None):
        self.called = False
        self.result = result
        self.args = None
        self.kwds = None
        return

    def __call__(self, *args, **kwds):
        self.called = True
        self.args = args
        self.kwds = kwds
        if isinstance(self.result, BaseException):
            raise self.result
        else:
            return self.result


class Editor(object):

    def __init__(self, flist=None, filename=None, key=None, root=None):
        self.text = Text()
        self.undo = UndoDelegator()

    def get_selection_indices(self):
        first = self.text.index('1.0')
        last = self.text.index('end')
        return (first, last)


class UndoDelegator(object):

    def undo_block_start(*args):
        pass

    def undo_block_stop(*args):
        pass
