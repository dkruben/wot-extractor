# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/tooltips/entry_point_tooltip.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from frameworks.wulf import ViewSettings as ViewSettings
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.lootbox_system.tooltips.entry_point_tooltip_view_model import EntryPointTooltipViewModel as EntryPointTooltipViewModel
from gui.impl.pub import ViewImpl as ViewImpl
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController

class EntryPointTooltip(ViewImpl):
    __slots__: tuple
    __lootBoxes: Any
    __eventName: Any
    def __init__(self, eventName):
        ...
    @property
    def viewModel(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __onLootBoxesStatusChanged(self):
        ...
    def __updateState(self):
        ...
    def __getEventExpireTime(self):
        ...
