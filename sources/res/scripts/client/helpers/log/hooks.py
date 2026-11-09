# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/helpers/log/hooks.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/helpers/log/hooks.py
from __future__ import absolute_import
import logging, traceback, sys, ResMgr

def formatException(excType, excValue, excTraceback):
    extracted = traceback.extract_tb(excTraceback)
    converted = []
    for filename, lineno, name, line in extracted:
        if filename.endswith('.py'):
            converted.append((
             ResMgr.resolveToAbsolutePath(filename), lineno, name, line))
        else:
            converted.append((filename, lineno, name, line))

    converted = traceback.format_list(converted)
    converted += traceback.format_exception(excType, excValue, None)
    return ('').join(converted)


def setupUserExceptionHook():

    def exceptionHook(excType, excValue, excTraceback):
        logging.critical(formatException(excType, excValue, excTraceback))

    sys.excepthook = exceptionHook
