# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/battle_queue.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/lobby/battle_queue.py
from __future__ import absolute_import
from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import RandomQueueProvider
from gui.impl import backport
from gui.impl.gen import R

class Comp7LightQueueProvider(RandomQueueProvider):

    def processQueueInfo(self, qInfo):
        info = dict(qInfo)
        allPlayersCount = info.get('players', 0)
        self._proxy.as_setDPS([
         {'type': (backport.text(R.strings.menu.prebattle.playersLabel())), 
            'icon': (backport.image(R.images.comp7_light.gui.maps.icons.icons.playersTotalIcon())), 
            'count': allPlayersCount, 
            'highlight': False}])

    def getLayoutStr(self):
        return 'comp7Light'

    def getIconPath(self, iconLabel):
        return backport.image(R.images.comp7_light.gui.maps.icons.battleTypes.c_136x136.comp7_light())

    def getTankInfoLabel(self):
        return ''

    def getTankIcon(self, vehicle):
        return ''

    def getTankName(self, vehicle):
        return ''

    def needAdditionalInfo(self):
        return False

    def additionalInfo(self):
        return ''
