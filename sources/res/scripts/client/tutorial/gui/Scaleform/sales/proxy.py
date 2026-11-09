# wot-extractor: codigo DESCOMPILADO de sources/res/scripts/client/tutorial/gui/Scaleform/sales/proxy.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: scripts/client/tutorial/gui/Scaleform/sales/proxy.py
from __future__ import absolute_import
from tutorial.gui import GUI_EFFECT_NAME
from tutorial.gui.Scaleform import effects_player
from tutorial.gui.Scaleform.lobby.proxy import SfLobbyProxy

class SfSalesProxy(SfLobbyProxy):

    def __init__(self):
        effects = {(GUI_EFFECT_NAME.SHOW_HINT): (effects_player.ShowChainHint()), 
           (GUI_EFFECT_NAME.SET_CRITERIA): (effects_player.SetCriteriaEffect()), 
           (GUI_EFFECT_NAME.SET_TRIGGER): (effects_player.SetTriggerEffect())}
        super(SfSalesProxy, self).__init__(effects_player.EffectsPlayer(effects))

    def getViewSettings(self):
        return {}

    def getViewsAliases(self):
        return {}
