# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/account_helpers/settings_core/settings_disable/disable_settings_ctrl.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any as _Any
from typing import TYPE_CHECKING as TYPE_CHECKING
from account_helpers.settings_core.settings_disable import aop as daop
from gui.prb_control.entities.listener import IGlobalListener as IGlobalListener
from helpers import dependency as dependency, aop as aop
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.game_control import IGameController as IGameController
from typing import Optional as Optional, Set as Set, Dict as Dict, Any as Any, Iterable as Iterable

class DisableSettingsController(IGameController, IGlobalListener):
    __settingsCore: _Any
    __keyToValConfig: _Any
    __keyToGUIPath: _Any
    __storageKeysToDisable: _Any
    _weaver: _Any
    __areSettingChanged: _Any
    def __init__(self):
        ...
    def init(self):
        ...
    def fini(self):
        ...
    def registerRecord(self, name, value, storages, guiPath, disable=True):
        ...
    def onDisconnected(self):
        ...
    def onAvatarBecomePlayer(self):
        ...
    def onLobbyInited(self, event):
        ...
    def onPrbEntitySwitched(self):
        ...
    def _canBeApplied(self):
        ...
    def __swapSettings(self):
        ...
    def __swapAfter(self):
        ...
    def _disable(self):
        ...
    def _enable(self):
        ...
    def __clearWeaver(self):
        ...
