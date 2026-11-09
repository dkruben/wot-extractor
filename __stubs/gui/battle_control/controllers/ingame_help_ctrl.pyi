# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/battle_control/controllers/ingame_help_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.daapi.settings.views import VIEW_ALIAS as VIEW_ALIAS
from gui.Scaleform.framework.entities.View import ViewKey as ViewKey
from gui.battle_control import event_dispatcher as gui_event_dispatcher
from skeletons.gui.app_loader import IAppLoader as IAppLoader
from helpers import dependency as dependency
from gui.battle_control.battle_constants import BATTLE_CTRL_ID as BATTLE_CTRL_ID
from gui.battle_control.controllers.interfaces import IBattleController as IBattleController
from gui.shared import g_eventBus as g_eventBus, EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import GameEvent as GameEvent
from gui.shared.system_factory import collectIngameHelpPagesBuilders as collectIngameHelpPagesBuilders
from Vehicle import Vehicle as Vehicle

class IngameHelpController(IBattleController):
    __slots__: tuple
    __appLoader: Any
    __arenaVisitor: Any
    __currentHintContext: Any
    def __init__(self, setup):
        ...
    def getControllerID(self):
        ...
    def startControl(self, *args):
        ...
    def stopControl(self):
        ...
    def showIngameHelp(self, vehicle):
        ...
    def canShow(self):
        ...
    def __onShowBtnHint(self, event):
        ...
    def __onHideBtnHint(self, _):
        ...
