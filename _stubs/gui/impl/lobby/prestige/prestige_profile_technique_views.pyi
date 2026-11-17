# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/prestige/prestige_profile_technique_views.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
import typing as typing
from constants import Configs as Configs
from frameworks.wulf import ViewFlags as ViewFlags, ViewSettings as ViewSettings, ViewStatus as ViewStatus
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.prestige.prestige_profile_technique_emblem_model import PrestigeProfileTechniqueEmblemModel as PrestigeProfileTechniqueEmblemModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_profile_technique_model import PrestigeProfileTechniqueModel as PrestigeProfileTechniqueModel
from gui.prestige.prestige_helpers import getCurrentProgress as getCurrentProgress, fillPrestigeEmblemModel as fillPrestigeEmblemModel, getNextGradeLevel as getNextGradeLevel, getVehiclePrestige as getVehiclePrestige
from gui.impl.lobby.prestige.prestige_level_grades_tooltip_view import PrestigeLevelGradesTooltipView as PrestigeLevelGradesTooltipView
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from shared_utils import nextTick as nextTick
from skeletons.gui.lobby_context import ILobbyContext as ILobbyContext
from skeletons.gui.shared import IItemsCache as IItemsCache
from frameworks.wulf import ViewEvent as ViewEvent, View as View
_logger: Any

class PrestigeProfileTechniqueCommon(ViewImpl):
    __slots__: tuple
    _itemsCache: Any
    _lobbyContext: Any
    _selectedVehIntCD: Any
    _databaseID: Any
    def __init__(self):
        ...
    def setDatabaseID(self, value):
        ...
    def setSelectedVehicleIntCD(self, value):
        ...
    def _getEvents(self):
        ...
    def _initialize(self, *args, **kwargs):
        ...
    def _createViewSettings(self):
        ...
    def _updateModel(self):
        ...
    def _checkData(self, method):
        ...
    def __onServerSettingsChange(self, diff):
        ...
    def __onSyncCompleted(self, *args):
        ...

class PrestigeProfileTechniqueView(PrestigeProfileTechniqueCommon):
    def setDatabaseID(self, value):
        ...
    def createToolTipContent(self, event, contentID):
        ...
    @property
    def viewModel(self):
        ...
    def _createViewSettings(self):
        ...
    def _updateModel(self):
        ...

class PrestigeProfileTechniqueEmblemView(PrestigeProfileTechniqueCommon):
    @property
    def viewModel(self):
        ...
    def _createViewSettings(self):
        ...
    def _updateModel(self):
        ...
