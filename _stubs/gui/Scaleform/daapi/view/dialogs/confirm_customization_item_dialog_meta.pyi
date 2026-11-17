# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/dialogs/confirm_customization_item_dialog_meta.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import math as math
from past.utils import old_div as old_div
import SoundGroups as SoundGroups
from CurrentVehicle import g_currentVehicle as g_currentVehicle
from gui.Scaleform.daapi.view.dialogs import IDialogMeta as IDialogMeta
from gui.Scaleform.daapi.view.lobby.customization.sound_constants import SOUNDS as SOUNDS
from gui.Scaleform.framework import ScopeTemplates as ScopeTemplates
from gui.shared import events as events
from gui.shared.tooltips import ACTION_TOOLTIPS_TYPE as ACTION_TOOLTIPS_TYPE
from helpers import i18n as i18n
from gui import SystemMessages as SystemMessages
from gui.Scaleform.locale.DIALOGS import DIALOGS as DIALOGS
from gui.shared.gui_items.processors.common import CustomizationsBuyer as CustomizationsBuyer
from gui.shared.money import Currency as Currency, CurrencyCollection as CurrencyCollection
from gui.shared.tooltips.formatters import packActionTooltipData as packActionTooltipData
from gui.shared.utils.decorators import adisp_process as adisp_process
from items.components.c11n_constants import MAX_ITEMS_FOR_BUY_OPERATION as MAX_ITEMS_FOR_BUY_OPERATION
from skeletons.gui.game_control import ISoundEventChecker as ISoundEventChecker
from skeletons.gui.shared import IItemsCache as IItemsCache
from helpers import dependency as dependency

class Types(object):
    BUY = 0
    SELL = 1

class ItemsCountStepSize(object):
    STANDART = 1

class ConfirmC11nBuyMeta(IDialogMeta):
    itemsCache: Any
    __soundEventChecker: Any
    __item: Any
    __title: Any
    __submitLabel: Any
    __cancelLabel: Any
    vehicle: Any
    type: Any
    def __init__(self, itemCD, title=..., submitBtn=..., cancelBtn=..., vehicle=None):
        ...
    def destroy(self):
        ...
    # decorador original: @adisp_process(...)
    def submit(self, item, count, _, vehicle):
        ...
    def getEventType(self):
        ...
    def getTitle(self):
        ...
    def getSubmitButtonLabel(self):
        ...
    def getCancelButtonLabel(self):
        ...
    def getItem(self):
        ...
    def getViewScopeType(self):
        ...
    def getActualPrices(self, item):
        ...
    def getCurrency(self, item):
        ...
    def getDefaultPrices(self, item):
        ...
    def getActionVO(self, item):
        ...
    def getDefaultValue(self, _):
        ...
    def getMaxAvailableItemsCount(self, item):
        ...
    def __getMaxCount(self, item, currency, balance):
        ...
    def getStepFactor(self, item):
        ...

class ConfirmC11nSellMeta(ConfirmC11nBuyMeta):
    __count: Any
    __handler: Any
    type: Any
    def __init__(self, itemCD, count, handler, title=..., submitBtn=..., cancelBtn=..., vehicle=None):
        ...
    def getEventType(self):
        ...
    def getMaxAvailableItemsCount(self, _):
        ...
    def getDefaultValue(self, _):
        ...
    def getActualPrices(self, item):
        ...
    def getDefaultPrices(self, item):
        ...
    def submit(self, item, count, _, vehicle):
        ...
    def getActionVO(self, item):
        ...
    def getStepFactor(self, item):
        ...
