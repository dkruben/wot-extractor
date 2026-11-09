# wot-extractor: codigo DESCOMPILADO de sources/res/comp7_light/scripts/client/comp7_light/gui/impl/lobby/__init__.pyc (uncompyle6 3.9.2 / Python 2.7.18) - nao e o codigo original
# uncompyle6 version 3.9.2
# Python bytecode version base 2.7 (62211)
# Decompiled from: Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 20 2020, 13:25:05) [MSC v.1500 64 bit (AMD64)]
# Embedded file name: comp7_light/scripts/client/comp7_light/gui/impl/lobby/__init__.py
from __future__ import absolute_import

def registerComp7LightLobby():
    from comp7_light_constants import PREBATTLE_TYPE
    from comp7_light.gui.comp7_light_constants import SELECTOR_BATTLE_TYPES
    from comp7_light.gui.game_control.award_controller import Comp7LightProgressionStageHandler, Comp7LightPunishWindowHandler
    from gui.game_control.platoon_controller import PlatoonController
    from gui.Scaleform.daapi.view.lobby.formatters.tooltips import _MODENAME_TO_PO_FILE
    from gui.shared.system_factory import registerAwardControllerHandlers
    registerAwardControllerHandlers((
     Comp7LightProgressionStageHandler, Comp7LightPunishWindowHandler))
    PlatoonController.SQUAD_SIZE_SELECT_PREBATTLE_TYPES.append(PREBATTLE_TYPE.COMP7_LIGHT)
    _MODENAME_TO_PO_FILE.update({(SELECTOR_BATTLE_TYPES.COMP7_LIGHT): 'comp7_light'})
