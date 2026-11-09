# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/BoosterInfoWindow.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/gui/Scaleform/daapi/view/lobby/BoosterInfoWindow.py
from __future__ import absolute_import
from gui.Scaleform import MENU
from gui.Scaleform.daapi.view.meta.BoosterInfoMeta import BoosterInfoMeta
from gui.Scaleform.framework.entities.View import View
from helpers import dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.goodies import IGoodiesCache

class BoosterInfoWindow(BoosterInfoMeta):
    goodiesCache = dependency.descriptor(IGoodiesCache)

    def __init__(self, ctx=None):
        super(BoosterInfoWindow, self).__init__()
        self.boosterID = ctx.get('boosterID')

    def onCancelClick(self):
        self.destroy()

    def onWindowClose(self):
        self.destroy()

    def _populate(self):
        super(View, self)._populate()
        booster = self.goodiesCache.getBooster(self.boosterID)
        self.as_setBoosterInfoS({'windowTitle': (_ms(MENU.BOOSTERS_COMMON_NAME)), 
           'name': (booster.userName), 
           'icon': (booster.icon), 
           'parameters': [
                        {'value': (('{}\n').format(booster.getFormattedValue())), 
                           'type': (('{}\n').format(_ms(MENU.BOOSTERS_COMMON_EFFECT_VALUE)))},
                        {'value': (booster.getEffectTimeStr(hoursOnly=True)), 
                           'type': (_ms(MENU.BOOSTERS_COMMON_EFFECT_TIME))}]})
