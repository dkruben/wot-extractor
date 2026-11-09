# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/shop/vehicle_sell_confirmation_popover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.daapi.view.meta.VehicleSellConfirmationPopoverMeta import VehicleSellConfirmationPopoverMeta as VehicleSellConfirmationPopoverMeta
from gui.Scaleform.locale.STORE import STORE as STORE
from gui.impl import backport as backport
from gui.shared.event_bus import EVENT_BUS_SCOPE as EVENT_BUS_SCOPE
from gui.shared.events import ShopEvent as ShopEvent
from gui.shared.formatters import text_styles as text_styles
from helpers import dependency as dependency
from helpers.i18n import makeString as _ms
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any

class VehicleSellConfirmationPopover(VehicleSellConfirmationPopoverMeta):
    itemsCache: Any
    __confirmGoldPrice: Any
    __tradeOffVehicleIntCD: Any
    def __init__(self, ctx=None):
        ...
    def confirmTradeIn(self):
        ...
    def _populate(self):
        ...
    def __getInitialVO(self):
        ...
