# wot-extractor: STUB (.pyi) gerado a partir de sources/res/scripts/client/gui/Scaleform/daapi/view/lobby/fortifications/FortReserveSelectPopover.py (arvore sintatica do codigo descompilado/original).
# So contem o que foi verificado no codigo: nomes, parametros, valores por omissao literais, docstrings e
# atributos atribuidos. 'Any' = tipo desconhecido; nenhuma assinatura, tipo ou comportamento foi inventado.

from typing import Any
import logging as logging
from gui.Scaleform.daapi.view.lobby.rally import vo_converters as vo_converters
from gui.Scaleform.daapi.view.meta.FittingSelectPopoverMeta import FittingSelectPopoverMeta as FittingSelectPopoverMeta
from gui.Scaleform.genConsts.FITTING_TYPES import FITTING_TYPES as FITTING_TYPES
from gui.impl import backport as backport
from gui.impl.gen import R as R
from gui.prb_control.entities.base.unit.listener import IUnitListener as IUnitListener
from gui.prb_control.items.stronghold_items import ARTILLERY_STRIKE as ARTILLERY_STRIKE, INSPIRATION as INSPIRATION
from gui.shared.events import CSReserveSelectEvent as CSReserveSelectEvent
from gui.shared.formatters import text_styles as text_styles
from gui.shared.items_parameters import params_helper as params_helper, formatters as formatters
from helpers import dependency as dependency
from skeletons.gui.shared import IItemsCache as IItemsCache
_logger: Any
RESERVE_PARAMS_LIST: dict

class FortReserveSelectPopover(FittingSelectPopoverMeta, IUnitListener):
    __itemsCache: Any
    _slotType: Any
    _slotIndex: Any
    _selectedIndex: Any
    def __init__(self, ctx=None):
        ...
    def setVehicleModule(self, newId, oldId, isRemove):
        ...
    def setCurrentTab(self, tabIndex):
        ...
    def _populate(self):
        ...
    def __buildModuleData(self, selectedIdxs, reserve, count):
        ...
    def __getReserveGroup(self):
        ...
    def __buildList(self):
        ...
    def __buildReserveParams(self, reserve):
        ...
