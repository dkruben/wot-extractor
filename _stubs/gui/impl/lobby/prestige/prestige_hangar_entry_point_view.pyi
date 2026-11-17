# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/prestige/prestige_hangar_entry_point_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from constants import Configs as Configs
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.prestige.prestige_hangar_entry_point_model import PrestigeHangarEntryPointModel as PrestigeHangarEntryPointModel
from gui.impl.pub import ViewImpl as ViewImpl
from gui.prestige.prestige_helpers import getCurrentProgress as getCurrentProgress, fillPrestigeEmblemModel as fillPrestigeEmblemModel, getVehiclePrestige as getVehiclePrestige, showPrestigeVehicleStats as showPrestigeVehicleStats, DEFAULT_PRESTIGE as DEFAULT_PRESTIGE
from helpers import dependency as dependency
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class PrestigeHangarEntryPointView(ViewImpl):
    __slots__: tuple
    __itemsCache: Any
    __lobbyContext: Any
    def __init__(self):
        ...
    @property
    def viewModel(self):
        ...
    def _getEvents(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def __updateModel(self):
        ...
    def __onShowInfoClick(self):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def __onCurrentVehicleChanged(self):
        ...
    def __onSyncCompleted(self, *args):
        ...
