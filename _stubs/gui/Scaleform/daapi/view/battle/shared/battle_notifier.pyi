# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/battle_notifier.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from account_helpers.settings_core.settings_constants import GAME as GAME
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.battle_control.controllers.arena_load_ctrl import IArenaLoadCtrlListener as IArenaLoadCtrlListener
from gui.battle_control.controllers.battle_notifier_ctrl import IBattleNotifierListener as IBattleNotifierListener
from gui.impl.battle.battle_notifier.battle_notifier_view import BattleNotifierView as BattleNotifierView
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

class BattleNotifier(InjectComponentAdaptor, IArenaLoadCtrlListener, IBattleNotifierListener):
    __slots__: tuple
    lobbyContext: Any
    settingsCore: Any
    __isArenaLoaded: Any
    __isEnabledByServer: Any
    def __init__(self):
        ...
    def _onPopulate(self):
        ...
    def _makeInjectView(self):
        ...
    def arenaLoadCompleted(self):
        ...
    def resultsNotificationReceived(self, results):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def _updateInjectedViewState(self):
        ...
    def _dispose(self):
        ...
