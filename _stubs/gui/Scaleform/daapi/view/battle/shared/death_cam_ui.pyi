# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/battle/shared/death_cam_ui.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.framework.entities.inject_component_adaptor import InjectComponentAdaptor as InjectComponentAdaptor
from gui.impl.battle.death_cam.death_cam_hud_view import DeathCamHudView as DeathCamHudView
from helpers import dependency as dependency
from skeletons.account_helpers.settings_core import ISettingsCore as ISettingsCore
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
_logger: Any

class DeathCamUI(InjectComponentAdaptor):
    __slots__: tuple
    lobbyContext: Any
    settingsCore: Any
    def _onPopulate(self):
        ...
    def _makeInjectView(self):
        ...
    def __onSettingsChanged(self, diff):
        ...
    def _updateInjectedViewState(self):
        ...
