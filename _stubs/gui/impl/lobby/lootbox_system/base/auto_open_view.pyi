# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/auto_open_view.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
from constants import LOOTBOX_TOKEN_PREFIX as LOOTBOX_TOKEN_PREFIX
from frameworks.wulf import ViewSettings as ViewSettings, WindowFlags as WindowFlags
from gui.impl.gen import R as R
from gui.impl.gen.view_models.views.lobby.lootbox_system.auto_open_view_model import AutoOpenViewModel as AutoOpenViewModel
from gui.impl.lobby.common.view_wrappers import createBackportTooltipDecorator as createBackportTooltipDecorator
from gui.impl.pub import ViewImpl as ViewImpl, WindowImpl as WindowImpl
from gui.lootbox_system.base.bonuses_helpers import REWARDS_GROUP_NAME_RES as REWARDS_GROUP_NAME_RES, RewardsGroup as RewardsGroup, getGoodiesFilter as getGoodiesFilter, getItemsFilter as getItemsFilter, getTankmenFilter as getTankmenFilter, getVehiclesFilter as getVehiclesFilter, isBattleBooster as isBattleBooster, isCrewBook as isCrewBook, noCompensation as noCompensation, isOptionalDevice as isOptionalDevice, packBonusGroups as packBonusGroups
from gui.lootbox_system.base.common import LOOTBOX_COMPENSATION_TOKEN_PREFIX as LOOTBOX_COMPENSATION_TOKEN_PREFIX
from gui.lootbox_system.base.decorators import createTooltipContentDecorator as createTooltipContentDecorator
from gui.lootbox_system.base.views_loaders import showItemPreview as showItemPreview
from helpers import dependency as dependency
from skeletons.gui.goodies import IGoodiesCache as IGoodiesCache

class AutoOpenView(ViewImpl):
    __goodiesCache: Any
    __eventName: Any
    __rewards: Any
    __boxes: Any
    __tooltips: Any
    def __init__(self, ctx):
        ...
    @property
    def viewModel(self):
        ...
    # decorador original: @createBackportTooltipDecorator(...)
    def createToolTip(self, event):
        ...
    # decorador original: @createTooltipContentDecorator(...)
    def createToolTipContent(self, event, contentID):
        ...
    def getTooltipData(self, event):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _getEvents(self):
        ...
    def __updateRewards(self):
        ...
    @classmethod
    def __getGroupsLayout(cls):
        ...
    def __showPreview(self, ctx):
        ...
    def __onClose(self):
        ...
    def __filterRewards(self, rewards):
        ...

class AutoOpenWindow(WindowImpl):
    def __init__(self, layer, ctx=None, *args, **kwargs):
        ...
