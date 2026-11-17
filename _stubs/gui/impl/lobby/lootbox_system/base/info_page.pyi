# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/lootbox_system/base/info_page.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from enum import Enum as Enum
from account_helpers.AccountSettings import LOOT_BOXES_SELECTED_BOX as LOOT_BOXES_SELECTED_BOX
from frameworks.wulf import WindowFlags as WindowFlags
from frameworks.wulf.view.array import fillIntsArray as fillIntsArray
from gui.Scaleform.Waiting import Waiting as Waiting
from gui.impl.gen import R as R
from gui.impl.pub.view_component import ViewComponent as ViewComponent
from gui.impl.gen.view_models.views.lobby.lootbox_system.box_model import BoxModel as BoxModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.info_page_model import InfoPageModel as InfoPageModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.slot_model import SlotModel as SlotModel
from gui.impl.pub import WindowImpl as WindowImpl
from gui.impl.wrappers.function_helpers import replaceNoneKwargsModel as replaceNoneKwargsModel
from gui.lootbox_system.base.bonuses_packers import packBonusModelAndTooltipData as packBonusModelAndTooltipData
from gui.lootbox_system.base.common import ViewID as ViewID, Views as Views
from gui.lootbox_system.base.decorators import createBackportTooltipDecorator as createBackportTooltipDecorator, createTooltipContentDecorator as createTooltipContentDecorator
from gui.lootbox_system.base.sound import playInfopageEnterSound as playInfopageEnterSound, playInfopageExitSound as playInfopageExitSound
from gui.lootbox_system.base.utils import getInfoPageSettings as getInfoPageSettings, isCountryForShowingExternalLootList as isCountryForShowingExternalLootList, isShopVisible as isShopVisible, openExternalLootList as openExternalLootList
from gui.lootbox_system.base.views_loaders import showItemPreview as showItemPreview
from helpers import dependency as dependency
from helpers.time_utils import getServerUTCTime as getServerUTCTime
from shared_utils import first as first
from skeletons.gui.game_control import ILootBoxSystemController as ILootBoxSystemController
from gui.shared.gui_items.loot_box import LootBox as LootBox

class _InfoPageSetting(str, Enum):
    VIDEO = 'isVideoVisible'

class InfoPage(ViewComponent):
    __lootBoxes: Any
    __baseWindowID = None
    __category: Any
    __eventName: Any
    __savedCategory: Any
    __tooltipData: Any
    def __init__(self, ctx=None):
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
    def _getBonusPacker(self):
        ...
    def _onLoading(self, *args, **kwargs):
        ...
    def _onLoaded(self, *args, **kwargs):
        ...
    def _finalize(self):
        ...
    def _getEvents(self):
        ...
    def __sortedSlotsIDs(self, slotsInfo):
        ...
    def __onStatusChange(self):
        ...
    def __onBoxesCountChange(self):
        ...
    def __fillChosenCategory(self, category='', box=None):
        ...
    def __updateCategory(self, ctx=None, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateState(self, model=None):
        ...
    # decorador original: @replaceNoneKwargsModel
    def __updateBoxes(self, model=None):
        ...
    def _setLootBox(self, box):
        ...
    def _setLootBoxSlot(self, probability, bonuses):
        ...
    def __showPreview(self, ctx):
        ...
    def __showShop(self):
        ...
    def __showIntroPage(self):
        ...
    def __showExternalLootList(self):
        ...
    def __onClose(self):
        ...

class InfoPageWindow(WindowImpl):
    def __init__(self, layer, ctx, **kwargs):
        ...
