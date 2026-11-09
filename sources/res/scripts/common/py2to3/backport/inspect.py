# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/py2to3/backport/inspect.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/py2to3/backport/inspect.py
from __future__ import absolute_import
import inspect
from future.utils import lmap
from py2to3.utils import PY3

def _joinseq(seq):
    if len(seq) == 1:
        return '(' + seq[0] + ',)'
    return '(' + (', ').join(seq) + ')'


def _strseq(obj, convert, join=_joinseq):
    if isinstance(obj, (list, tuple)):
        return join(lmap((lambda o, c=convert, j=join: _strseq(o, c, j)), obj))
    return convert(obj)


def getargspec(func):
    if PY3:
        return inspect.getfullargspec(func)
    return inspect.getargspec(func)


def formatargspec(args, varargs=None, varkw=None, defaults=None, kwonlyargs=None, kwonlydefaults=None, annotations=None, formatarg=str, formatvarargs=(lambda name: '*' + name), formatvarkw=(lambda name: '**' + name), formatvalue=(lambda value: '=' + repr(value)), join=_joinseq):
    specs = []
    if defaults:
        firstdefault = len(args) - len(defaults)
    for i, arg in enumerate(args):
        spec = _strseq(arg, formatarg, join)
        if defaults and i >= firstdefault:
            spec = spec + formatvalue(defaults[i - firstdefault])
        specs.append(spec)

    if varargs is not None:
        specs.append(formatvarargs(varargs))
    if varkw is not None:
        specs.append(formatvarkw(varkw))
    return '(' + (', ').join(specs) + ')'
