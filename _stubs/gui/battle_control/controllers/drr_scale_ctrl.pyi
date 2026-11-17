# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/drr_scale_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import weakref as weakref
import BigWorld as BigWorld
import Keys as Keys
from Event import Event as Event
from account_helpers.settings_core.settings_constants import GRAPHICS as GRAPHICS
from gui import g_repeatKeyHandlers as g_repeatKeyHandlers
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from helpers import dependency as dependency
from helpers import drr_scale as drr_scale
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore

class DRRScaleController(IBattleController):
    settingsCore: Any
    __messages: Any
    onDRRChanged: Any
    def __init__(self, messages):
        ...
    def getControllerID(self):
        ...
    def startControl(self):
        ...
    def stopControl(self):
        ...
    def handleKey(self, key, isDown):
        ...
    def __handleRepeatKeyEvent(self, event):
        ...
