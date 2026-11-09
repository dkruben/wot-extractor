# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/items/writers/gun_writers.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/items/writers/gun_writers.py
from __future__ import absolute_import
from items import _xml
from items.writers import shared_writers

def writeRecoilEffect(item, section, cache):
    if item is None:
        return
    else:
        if item.effectName != 'none':
            _xml.rewriteString(section, 'recoilEffect', item.effectName)
            section.deleteSection('backoffTime')
            section.deleteSection('returnTime')
        else:
            _xml.rewriteFloat(section, 'backoffTime', item.backoffTime)
            _xml.rewriteFloat(section, 'returnTime', item.returnTime)
            section.deleteSection('recoilEffect')
        _xml.rewriteFloat(section, 'amplitude', item.amplitude)
        shared_writers.writeLodDist(item.lodDist, section, 'lodDist', cache)
        return
