# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/impl/lobby/dialogs/auxiliary/confirmed_item.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import typing as typing
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES as FITTING_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.impl.gen.view_models.constants.item_highlight_types import ItemHighlightTypes as ItemHighlightTypes
from gui.impl.lobby.dialogs.auxiliary.confirmed_item_helpers import getHighlightsTypeByItem as getHighlightsTypeByItem, getOverlayTypeByItem as getOverlayTypeByItem, ConfirmedItemWarningTypes as ConfirmedItemWarningTypes, DependsOnDevicesWarning as DependsOnDevicesWarning, PairModificationsWillBeDemount as PairModificationsWillBeDemount
from gui.impl.wrappers.user_compound_price_model import BuyPriceModelBuilder as BuyPriceModelBuilder
from gui.shared.gui_items import GUI_ITEM_TYPE as GUI_ITEM_TYPE
from gui.shared.utils.requesters import REQ_CRITERIA as REQ_CRITERIA
from gui.impl.gen.view_models.views.lobby.common.confirmed_item_model import ConfirmedItemModel as ConfirmedItemModel
from helpers import dependency as dependency
from post_progression_common import ACTION_TYPES as ACTION_TYPES
from skeletons.gui.game_control import IWotPlusController as IWotPlusController
from skeletons.gui.shared import IItemsCache as IItemsCache
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_EMPTY as ITEM_PRICE_EMPTY
from gui.shared.gui_items.fitting_item import FittingItem as FittingItem
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from gui.veh_post_progression.models.modifications import PostProgressionActionItem as PostProgressionActionItem
SUPPORTED_TYPES: Any
CTX_VEHICLE_INV_ID = 'vehicleInvID'

class ConfirmedItem(object):
    __slots__: tuple
    _item: Any
    _ctx: Any
    _warnings: Any
    def __init__(self, item, ctx=None):
        ...
    def getName(self):
        ...
    def getTypeID(self):
        ...
    def getImageSource(self):
        ...
    def getHighlightsType(self):
        ...
    def getOverlayType(self):
        ...
    def getWarnings(self):
        ...
    def getRemovalPrice(self):
        ...
    def canUseDemountKit(self):
        ...
    def getOptItemDescKey(self):
        ...
    def getLevel(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...
    def getCofirmedItemViewModel(self):
        ...
    def _setWarnings(self):
        ...

class ConfirmedArtefact(ConfirmedItem):
    def getImageSource(self):
        ...
    def getHighlightsType(self):
        ...
    def getOverlayType(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...

class ConfirmedOptDevice(ConfirmedArtefact):
    __itemsCache: Any
    __wotPlus: Any
    def getRemovalPrice(self):
        ...
    def canUseDemountKit(self):
        ...
    def getOptItemDescKey(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...

class ConfirmedBattleBooster(ConfirmedArtefact):
    __itemsCache: Any
    def getOverlayType(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...
    def _setWarnings(self):
        ...
    def __getBoosterReplaceCriteria(self, vehInvID):
        ...

class ConfirmedBattleAbility(ConfirmedItem):
    def getHighlightsType(self):
        ...
    def getImageSource(self):
        ...
    def getLevel(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...

class ConfirmedModule(ConfirmedItem):
    def getImageSource(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...

class ConfirmedDualGun(ConfirmedModule):
    def getImageSource(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...

class ConfirmedShell(ConfirmedItem):
    def getImageSource(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...

class ConfirmedPostProgressionActionItem(ConfirmedItem):
    __itemsCache: Any
    def getName(self):
        ...
    def getImageSource(self):
        ...
    def getLevel(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...

class ConfirmedPostProgressionPairModification(ConfirmedPostProgressionActionItem):
    __itemsCache: Any
    def getImageSource(self):
        ...
    def getHighlightsType(self):
        ...
    @classmethod
    def createFromGUIItem(cls, item, ctx=None):
        ...
    def _setWarnings(self):
        ...
