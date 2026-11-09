# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/wrappers/function_helpers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/wrappers/function_helpers.py
from __future__ import absolute_import
from functools import wraps

def replaceNoneKwargsModel(func):

    @wraps(func)
    def wrapper(self, *args, **kwargs):
        actual = kwargs.get('model')
        if actual is None:
            with self.getViewModel().transaction() as model:
                kwargs['model'] = model
                return func(self, *args, **kwargs)
        else:
            return func(self, *args, **kwargs)
        return

    return wrapper
