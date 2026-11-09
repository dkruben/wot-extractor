# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/battle/messages/player_messages.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/Scaleform/daapi/view/battle/messages/player_messages.py
from __future__ import absolute_import
from comp7_core.gui.Scaleform.daapi.view.battle.messages.player_messages import Comp7CorePlayerMessages
from helpers import dependency
from skeletons.gui.game_control import IComp7LightController

class Comp7LightPlayerMessages(Comp7CorePlayerMessages):
    __comp7LightController = dependency.descriptor(IComp7LightController)

    @property
    def _modeController(self):
        return self.__comp7LightController
