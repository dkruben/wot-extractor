# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/vehicles/entities/vehicle_models/client_shot_params.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/vehicles/entities/vehicle_models/client_shot_params.py
from __future__ import absolute_import
import typing
from helpers_common import reprSlots

class ShotParams(object):
    __slots__ = ('sourceID', 'gunIndexDelayed', 'shellKindIdx', 'predictShooting')

    def __init__(self, sourceID, gunIndexDelayed, shellKindIdx, predictShooting):
        self.sourceID = sourceID
        self.gunIndexDelayed = gunIndexDelayed
        self.shellKindIdx = shellKindIdx
        self.predictShooting = predictShooting

    __repr__ = reprSlots
