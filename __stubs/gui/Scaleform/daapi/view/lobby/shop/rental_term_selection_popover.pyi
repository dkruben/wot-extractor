# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/shop/rental_term_selection_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import constants as constants
from constants import RentType as RentType, GameSeasonType as GameSeasonType
from rent_common import parseRentID as parseRentID, isWithinMaxRentTime as isWithinMaxRentTime, SeasonRentDuration as SeasonRentDuration
from soft_exception import SoftException as SoftException
from gui.impl import backport as backport
from gui.impl.gen.resources import R as R
from gui.Scaleform.daapi.view.meta.RentalTermSelectionPopoverMeta import RentalTermSelectionPopoverMeta as RentalTermSelectionPopoverMeta
from gui.Scaleform.locale.STORE import STORE as STORE
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ShopEvent as ShopEvent
from gui.shared.formatters import text_styles as text_styles, getItemPricesVO as getItemPricesVO, getMoneyVO as getMoneyVO
from gui.shared.money import Money as Money
from gui.shared.gui_items.gui_item_economics import ItemPrice as ItemPrice
from helpers import dependency as dependency, i18n as i18n
from skeletons.gui.shared import IItemsCache as IItemsCache
_NOT_RENT_IDX = -1
_SEASON_RENT_TERMS: dict

class RentalTermSelectionPopover(RentalTermSelectionPopoverMeta):
    itemsCache: Any
    __vehicleIntCD: Any
    __selectedRentID: Any
    def __init__(self, ctx=None):
        ...
    def selectTerm(self, itemId):
        ...
    def _populate(self):
        ...
    def __onItemCacheSyncCompleted(self, *args):
        ...
    def __getInitialVO(self):
        ...
