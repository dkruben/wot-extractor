# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/common/filter_contexts.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/common/filter_contexts.py
from __future__ import absolute_import

class FilterSetupContext(object):

    def __init__(self, ctx=None, asset=None):
        self.ctx = ctx or {}
        self.asset = asset or ''
        self.asset = self.asset.format(**self.ctx)


def getFilterSetupContexts(xpRateMultiplier):
    return {'favorite': (FilterSetupContext(asset='favorite')), 
       'elite': (FilterSetupContext(asset='elite_small_icon')), 
       'premium': (FilterSetupContext(asset='prem_small_icon')), 
       'igr': (FilterSetupContext(asset='premium_small')), 
       'bonus': (FilterSetupContext(ctx={'multiplier': xpRateMultiplier}, asset='bonus_x{multiplier}')), 
       'battleRoyale': (FilterSetupContext(asset='battle_royale_toggle')), 
       'rented': (FilterSetupContext(asset='marathon/time_icon'))}


def getFilterPopoverSetupContexts(xpRateMultiplier):
    return {'favorite': (FilterSetupContext(asset='favorite_medium')), 
       'elite': (FilterSetupContext(asset='elite_small_icon')), 
       'premium': (FilterSetupContext(asset='prem_small_icon')), 
       'igr': (FilterSetupContext(asset='premium_igr_small')), 
       'bonus': (FilterSetupContext(ctx={'multiplier': xpRateMultiplier}, asset='bonus_x')), 
       'rented': (FilterSetupContext(asset='marathon/time_icon')), 
       'event': (FilterSetupContext(asset='event_small_icon')), 
       'isCommonProgression': (FilterSetupContext(asset='common_progression')), 
       'crystals': (FilterSetupContext(asset='bons_small')), 
       'clanRented': (FilterSetupContext(asset='clan_wars')), 
       'ranked': (FilterSetupContext(asset='ranked'))}
