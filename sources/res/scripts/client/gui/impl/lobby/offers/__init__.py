# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/impl/lobby/offers/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/impl/lobby/offers/__init__.py
import typing
from constants import GF_RES_PROTOCOL
from gui.shared.utils.functions import getAbsoluteUrl

def getGfImagePath(imgPath):
    if imgPath is None:
        return
    else:
        newPath = getAbsoluteUrl(imgPath)
        newPath = newPath.replace('\\', '/')
        if not newPath.startswith(GF_RES_PROTOCOL.IMG):
            newPath = ('').join([GF_RES_PROTOCOL.IMG, newPath])
        return newPath
