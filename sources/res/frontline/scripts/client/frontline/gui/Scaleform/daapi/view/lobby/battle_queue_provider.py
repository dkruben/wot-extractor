# wot-extractor: codigo DESCOMPILADO de sources/res/frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/battle_queue_provider.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: frontline/scripts/client/frontline/gui/Scaleform/daapi/view/lobby/battle_queue_provider.py
from __future__ import absolute_import
import BigWorld
from gui.Scaleform.daapi.view.lobby.battle_queue.battle_queue import RandomQueueProvider
from gui.Scaleform.locale.MENU import MENU
from helpers.i18n import makeString

class EpicQueueProvider(RandomQueueProvider):

    def forceStart(self):
        currPlayer = BigWorld.player()
        if currPlayer is not None:
            currPlayer.FLAccountComponent.forceEpicDevStart()
        return

    def getTankInfoLabel(self):
        return makeString(MENU.PREBATTLE_STARTINGTANKLABEL)
