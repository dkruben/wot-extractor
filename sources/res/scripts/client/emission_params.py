# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/emission_params.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/emission_params.py
from __future__ import absolute_import
from collections import namedtuple
EmissionParams = namedtuple('EmissionParams', ('emissionTexture', 'emissionDeferredPower',
                                               'emissionForwardPower'))
EmissionParams.__new__.__defaults__ = ('', 1.0, 1.0)

def getEmissionParams(item):
    if item is not None and item.emissionParams is not None and item.emissionParams.emissionTexture:
        return EmissionParams(emissionTexture=item.emissionParams.emissionTexture, emissionDeferredPower=item.emissionParams.emissionDeferredPower, emissionForwardPower=item.emissionParams.emissionForwardPower)
    else:
        return
