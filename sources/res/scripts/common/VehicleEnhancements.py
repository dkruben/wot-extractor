# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/common/VehicleEnhancements.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/common/VehicleEnhancements.py
from __future__ import absolute_import
from future.utils import viewvalues
from items.vehicles import EnhancementItem

class VehicleEnhancements(object):

    def __init__(self, enhancements):
        self.factors = []
        for items in viewvalues(enhancements):
            for enhancement in viewvalues(items):
                if 'factors' in enhancement:
                    self.factors.extend([EnhancementItem(factor['name'], factor['value'], factor['operation']) for factor in enhancement['factors']])

    def onCollectFactors(self, factors):
        for factor in self.factors:
            factors[factor.name] = factor.applyFactor(factors[factor.name])
